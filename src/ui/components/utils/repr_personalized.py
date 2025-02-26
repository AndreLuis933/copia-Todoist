def ReprPersonalized(cls):
    original_str = cls.__str__
    original_repr = cls.__repr__

    def new_str(self):
        return f"{self.__class__.__name__} {original_str(self)}"

    def new_repr(self):
        return f"{self.__class__.__name__}({original_repr(self)})"

    cls.__str__ = new_str
    cls.__repr__ = new_repr
    return cls