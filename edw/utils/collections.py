from collections import OrderedDict

# since python 3.6 both OrderedDict and defaultdict come with their own __slots__
# this makes inheriting from both impossible "TypeError: multiple bases have instance lay-out conflict"
# Thus we implement our own defaultdict and inherit only from OrderedDict.
# Note that in python3.6 all dicts are ordered, but this is an implementation detail and we don't have methods
# like move_to_end on bare dict and defaultdict
class DefaultOrderedDict(OrderedDict):
    """
    A combination of collections.OrderedDict and collections.defaultdict.

    >>> d = DefaultOrderedDict(lambda: 0)
    >>> d['z'] += 1
    >>> d['y'] = 2
    >>> 'x' in d
    False
    >>> d['x']
    0
    >>> list(d.items())
    [('z', 1), ('y', 2), ('x', 0)]

    >>> d = DefaultOrderedDict((('z', 1), ('y', 2)), default_factory=(lambda: 0))
    >>> d['x'] == 0
    True
    >>> list(d.items())
    [('z', 1), ('y', 2), ('x', 0)]

    >>> d = DefaultOrderedDict(lambda: 0, (('z', 1), ('y', 2)))
    >>> d['x']
    0
    >>> list(d.items())
    [('z', 1), ('y', 2), ('x', 0)]

    >>> DefaultOrderedDict()['x']
    Traceback (most recent call last):
      ...
    KeyError: 'x'

    """
    # Source: http://stackoverflow.com/a/6190500/562769
    # with own modifications to make all methods actually work
    def __init__(self, *args, **kwargs):
        default_factory = None
        try:
            default_factory = kwargs.pop('default_factory')
        except KeyError:
            if args and callable(args[0]):
                default_factory = args[0]
                args = args[1:]

        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return self.__class__, args, None, None, iter(self.items())

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return self.__class__(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy
        return self.__class__(self.default_factory,
                              copy.deepcopy(iter(self.items())))

    def __repr__(self):
        return 'DefaultOrderedDict(%s, %s)' % (self.default_factory,
                                               OrderedDict.__repr__(self))
