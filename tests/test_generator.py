from io import StringIO
from src import number_generator
from pytest import MonkeyPatch, raises
from src.number_generator import COMMANDS, command, process_command


def test_register_command():
    """Tests whether registering a callback as a command
    has an effect on the COMMANDS dictionary"""
    _ = command("get_zero")(lambda: 0)
    assert COMMANDS["get_zero"]() == 0


def mock_command(cmd: str) -> str:
    """Mocks the stdin and stdout streams, passing the given
    command to stdin, calling process_command and returning the
    output from stdout"""
    mp = MonkeyPatch()
    mp.setattr(number_generator, "stdin", StringIO(f"{cmd}\n"))

    mock_stdout = StringIO()
    mp.setattr(number_generator, "stdout", mock_stdout)

    process_command()
    return mock_stdout.getvalue().strip("\n")


def test_hi():
    '''Output from the "Hi" command should be "Hi"'''
    assert mock_command("Hi") == "Hi"


def test_shutdown():
    """Calling the "Shutdown" command should raise SystemExit"""
    with raises(SystemExit):
        mock_command("Shutdown")


def test_getrandom(monkeypatch: MonkeyPatch):
    """Output from the "GetRandom" command should be a random number, castable to int"""
    monkeypatch.setattr(number_generator, "randint", lambda *_: 1)
    assert int(mock_command("GetRandom")) == 1
