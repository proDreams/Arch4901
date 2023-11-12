# Переписать код в соответствии с Interface Segregation Principle:

from abc import ABC, abstractmethod
import math


class TwoDimensionalShape(ABC):
    @abstractmethod
    def area(self):
        pass


class ThreeDimensionalShape(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(ThreeDimensionalShape):
    def __init__(self, edge):
        self.edge = edge

    def volume(self):
        return self.edge * self.edge * self.edge

    def area(self):
        return 6 * self.edge * self.edge
