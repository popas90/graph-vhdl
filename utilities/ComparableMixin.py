class ComparableMixin:
    # When using this mixin, implement _cmpkey(self) to return a tuple of
    # all the properties used for comparing the objects

    def _compare(self, other, method):
        try:
            return method(self._cmpkey(), other._cmpkey())
        except(AttributeError, TypeError):
            # _cmpkey not implemented or return different type
            return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s, o: s != o)
