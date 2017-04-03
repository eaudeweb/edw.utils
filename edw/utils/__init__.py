from collections import Iterable


def is_iter(v):
    """Returns True only for non-string iterables."""
    return not isinstance(v, str) and isinstance(v, Iterable)
