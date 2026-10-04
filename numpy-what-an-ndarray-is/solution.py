import numpy as np


def describe_ndarray_basics(arr: np.ndarray) -> dict:
    """
    Given a NumPy array `arr`, return a dictionary with two keys:
      - "dtype": the array's dtype, as a string (e.g. "int64")
      - "itemsize": the number of bytes each single element
        occupies in the underlying buffer (arr.itemsize)
    """
    return {
        "dtype": str(arr.dtype),
        "itemsize": arr.itemsize
    }
