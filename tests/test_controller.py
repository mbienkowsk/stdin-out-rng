from io import TextIOWrapper, BytesIO
import subprocess
from pytest import MonkeyPatch, fixture
from src.controller import *
from dataclasses import dataclass, field


@dataclass
class MockPopen:
    stdin: TextIOWrapper = field(default=TextIOWrapper(BytesIO()))
    stdout: TextIOWrapper = field(default=TextIOWrapper(BytesIO()))


@fixture
def mock_subprocess(
    monkeypatch: MonkeyPatch,
) -> Popen:
    """Injects a clean mock Popen instance into a test"""
    monkeypatch.setattr(subprocess, "Popen", MockPopen)
    subproc = subprocess.Popen()  # type: ignore
    return subproc


def test_send_message(mock_subprocess):
    send_message(mock_subprocess, "hello there!")
    mock_subprocess.stdin.seek(0)
    assert mock_subprocess.stdin.readline() == "hello there!\n"


def test_read_message(mock_subprocess):
    mock_subprocess.stdout = TextIOWrapper(BytesIO(b"goodbye!\n"))
    assert read_message(mock_subprocess) == "goodbye!"
