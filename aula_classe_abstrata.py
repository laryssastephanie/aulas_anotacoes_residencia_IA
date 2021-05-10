from math import *
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def desenhe(self):
        pass

f1 = FormaGeometrica(0, 0)
f1.desenhe()

class Forma2D(FormaGeometrica):
    def __init__(self, x, y):
        super().__init__(x, y)

