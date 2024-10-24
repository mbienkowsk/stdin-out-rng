import io
from subprocess import Popen, PIPE
from contextlib import contextmanager
import shlex


HI_MSG = "Hi"
RAND_MSG = "GetRandom"
SHUTDOWN_MSG = "Shutdown"
N_NUMS = 100


def send_message(proc: Popen, msg: str):
    """Sends a message to the subprocess"""
    assert isinstance(proc.stdin, io.TextIOWrapper)
    proc.stdin.write(msg + "\n")
    proc.stdin.flush()


def read_message(proc: Popen):
    """Reads a newline-separated message from the subprocess"""
    assert isinstance(proc.stdout, io.TextIOWrapper)
    return proc.stdout.readline().strip("\n")


def generate_randint(proc: Popen):
    """Asks the generator for a random int and returns it"""
    send_message(proc, RAND_MSG)
    return int(read_message(proc))


@contextmanager
def random_number_generator(generator_cmd):
    """Launches the subprocess and gracefully terminates it after the user is done with it"""
    proc = Popen(shlex.split(generator_cmd), stdin=PIPE, stdout=PIPE, text=True)
    try:
        yield proc
    finally:
        send_message(proc, SHUTDOWN_MSG)
