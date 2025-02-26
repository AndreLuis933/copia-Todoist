class ReprPersonalized:
    # Magic methods    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}"