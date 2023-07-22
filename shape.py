from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def compute_area(self):
        pass