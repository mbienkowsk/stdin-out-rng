from argparse import ArgumentParser, Namespace
from statistics import mean, median

from src.controller import (
    generate_randint,
    random_number_generator,
    read_message,
    send_message,
)

HI_MSG = "Hi\n"
RAND_MSG = "GetRandom\n"
SHUTDOWN_MSG = "Shutdown\n"
N_NUMS = 100


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "generator_launch_cmd",
        type=str,
        default="python3 src/number_generator.py",
        nargs="?",
        help="Command that, when launched, runs the random number generator",
    )
    return parser.parse_args()


def main():
    generator_cmd = parse_args().generator_launch_cmd

    with random_number_generator(generator_cmd) as gen:
        send_message(gen, HI_MSG)
        assert read_message(gen) == "Hi"

        nums = sorted([generate_randint(gen) for _ in range(N_NUMS)])
        print(nums)
        print(f"Median: {median(nums)}")
        print(f"Average: {mean(nums)}")


if __name__ == "__main__":
    main()
