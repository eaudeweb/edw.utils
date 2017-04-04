from collections import Iterable


def is_iter(v):
    """Returns True only for non-string iterables.

    >>> is_iter('abc')
    False
    >>> is_iter({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_iter(map(lambda x: x, 'abc'))
    True
    """
    return not isinstance(v, str) and isinstance(v, Iterable)
