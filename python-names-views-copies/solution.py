class View:
    """
    A window onto a shared list.
    """

    def __init__(self, buffer, indices=None):
        self.buffer = buffer
        self.indices = range(len(buffer)) if indices is None else indices

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.buffer[self.indices[key]]

        if isinstance(key, slice):
            return View(self.buffer, self.indices[key])

        raise TypeError("key must be an int or slice")

    def __setitem__(self, key, value):
        self.buffer[self.indices[key]] = value

    def to_list(self):
        return [self.buffer[i] for i in self.indices]


def shares_buffer(a, b) -> bool:
    return a.buffer is b.buffer


def scale_in_place(view, k) -> None:
    for i in range(len(view)):
        view[i] = view[i] * k


def scaled_copy(view, k) -> list:
    return [value * k for value in view.to_list()]
