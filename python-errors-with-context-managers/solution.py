from contextlib import contextmanager


class Recorder:
    """
    A context manager that records events in a list.
    """

    def __init__(self, log):
        self.log = log

    def __enter__(self):
        self.log.append("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.log.append("exit")

        if exc_type is not None:
            self.log.append(f"error:{exc_type.__name__}")

        return False


class SuppressAndRecord:
    """
    A context manager that suppresses one kind of exception.
    """

    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        self.caught = None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if (
            exc_type is not None
            and issubclass(exc_type, self.exception_type)
        ):
            self.caught = exc_value
            return True

        return False


@contextmanager
def temporary_value(settings: dict, key, value):
    """
    Temporarily change settings[key], restoring the original value
    even if an exception occurs.
    """
    previous_value = settings[key]
    settings[key] = value

    try:
        yield
    finally:
        settings[key] = previous_value


def write_lines(path: str, lines: list) -> None:
    """
    Write each string in lines to the file, one per line.
    """
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path: str) -> list:
    """
    Read lines and remove their trailing newline.
    """
    with open(path, "r") as f:
        return [line.rstrip("\n") for line in f]
