from typing import Callable
from random import randint
from collections import defaultdict
from sys import stdin, stdout

# Registered commands. Default command callback - one that does nothing
COMMANDS: defaultdict[str, Callable] = defaultdict(lambda: lambda: ...)


def command(cmd_name: str) -> Callable:
    """Used to register functions as command-executing callbacks"""

    def wrapper(func: Callable):
        COMMANDS[cmd_name] = func
        return func

    return wrapper


@command("Hi")
def hi():
    stdout.write("Hi\n")
    stdout.flush()


@command("GetRandom")
def get_random():
    stdout.write(f"{randint(1,100)}\n")
    stdout.flush()


@command("Shutdown")
def shutdown():
    raise SystemExit(0)


def process_command():
    """Reads a single command from stdin and executes
    the corresponding callback"""
    cmd = stdin.readline().strip("\n")
    callback = COMMANDS[cmd]
    callback()


if __name__ == "__main__":
    # Process commands in a loop until Shutdown is received
    while True:
        process_command()
