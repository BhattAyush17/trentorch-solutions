class Vec:
    """
    A fixed sequence of numbers.
    """

    def __init__(self, *components):
        self.data = list(components)

    def __repr__(self):
        return f"Vec({', '.join(map(str, self.data))})"

    def __eq__(self, other):
        if not isinstance(other, Vec):
            return NotImplemented

        return self.data == other.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index]

        if isinstance(index, slice):
            return Vec(*self.data[index])

        raise TypeError("index must be an int or slice")
