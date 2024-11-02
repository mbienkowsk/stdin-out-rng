from io import TextIOWrapper, BytesIO
import subprocess
from pytest import MonkeyPatch, fixture
from src.controller import *
from dataclasses import dataclass, field


@dataclass
class MockPopen:
    """A wrapper around stdin and stdout mocks, substituted
    for subproces.Popen"""

    stdin: TextIOWrapper = field(default=TextIOWrapper(BytesIO()))
    stdout: TextIOWrapper = field(default=TextIOWrapper(BytesIO()))


@fixture
def mock_subprocess(
    monkeypatch: MonkeyPatch,
) -> Popen:
    """Injects a clean mock Popen instance into a test"""
    monkeypatch.setattr(subprocess, "Popen", MockPopen)
    subproc = subprocess.Popen()  # type: ignore - Popen's init signature is different
    return subproc


def test_send_message(mock_subprocess):
    """A message sent to the subprocess should be readable from its stdin"""
    send_message(mock_subprocess, "hello there!")
    mock_subprocess.stdin.seek(0)
    assert mock_subprocess.stdin.readline() == "hello there!\n"


def test_read_message(mock_subprocess):
    """A message from the subprocess should be readable from its stdout"""
    mock_subprocess.stdout = TextIOWrapper(BytesIO(b"goodbye!\n"))
    assert read_message(mock_subprocess) == "goodbye!"
