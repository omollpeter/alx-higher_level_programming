#!/usr/bin/python3
from add_0 import add


def use_add(a, b):
    """Use add function - Uses add function from a module

    Args:
        a: First integer
        b: Second integer

    Returns:
        return value - Nothing
    """
    print("{0} + {1} = {2}".format(a, b, add(a, b)))


if __name__ == "__main__":
    use_add(1, 2)
