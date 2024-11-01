## Stdin/out based RNG

To run:

```shell
python3 main.py
```

### Program A (`number_generator.py`)

A simple program parsing given pagebreak-separated commands from the stdin and responding to them.
Made to be extensible and readable using a registering decorator. It's used to generate random ints
from the range [1..100].

### Program B (`controller.py`)

This program receives a path to the generator executable from the user, launches it as a
separate process and communicates with it using stdin/out. I assumed that program A's messages are also supposed to be page break
separated. Note that any command/executable can be passed to the controller, as long as it fulfills the generator's interface, so
the controller is completely decoupled from a specific generator. The controller uses a context manager interface to initialize and teardown the
generator, so it will always get closed gracefully, even if an error derails the controller.
