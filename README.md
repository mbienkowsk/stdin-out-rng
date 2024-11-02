## Stdin/out based RNG

Help for the main executable:

```shell
python3 main.py --help
```

Ran by:

```shell
python3 main.py
```

Tests ran by:

```shell
pytest
```

### Program A (`number_generator.py`)

A simple program parsing given pagebreak-separated commands from the stdin and responding to them.
Made to be extensible and readable using a registering decorator.

### Program B (`controller.py`)

This program launches the generator as a subprocess using the provided command and communicates with it
using stdin/out. I

This program launches the generator as a separate process separate process and communicates with it using stdin/out.
I assumed that program A's messages are also supposed to be page break separated.
Note that any command/executable can be passed to the controller, as long as it fulfills the generator's interface, so
the controller is completely decoupled from a specific generator. The controller uses a context manager interface to initialize and tear the
generator down, so it will always get closed gracefully, even if an exception was to derail the controller.

### `main.py`

In the main function we:

* Send the Hi command to Program A and verify the correct response.
* Retrieve 100 random numbers by sending the GetRandom command to Program A 100 times.
* Send the Shutdown command to Program A to terminate it gracefully.
* Sort the list of retrieved random numbers and print the sorted list to the console.
* Calculate and print the median and average of the numbers.

The generator command is passed as a command line argument, defaulting to `python3 src/number_generator.py`

### Unit tests (`tests/`)

* Generator tests test the functionality of all of the defined commands, as well as defining a new one
* Controller tests use an injected MockPopen object to test whether the expected input is read
and written from its stdin and stdout streams when using `read-` and `write_message`
