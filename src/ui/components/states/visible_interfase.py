from abc import ABC, abstractmethod

class VisibleState(ABC):
    @abstractmethod
    def mostar(self, component):
        pass

    @abstractmethod
    def esconder(self, component):
        pass
    