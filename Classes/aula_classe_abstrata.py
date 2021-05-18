from abc import ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def calcula_area(self):
        pass

class Triangulo(Poligono):
    def __init__(self, base=1, altura=1):
        self.base, self.altura = base, altura

    def calcula_area(self): # precisa ter os mesmos métodos da classe abstrata, caso contrário, não será instanciada
        return self.base*self.altura/2

t1 = Triangulo()
print(t1.calcula_area())

# Escondendo a Implementação - Convenções

class Triangulo:
    def __init__(self, base=1, altura=1):
        self._base, self._altura = base, altura # 1 underscore = protegido / somente pode ser acessado dentro da própria classe ou pelas classes filhas.

t1 = Triangulo()


class EquiTriang(Triangulo):
    def __init__(self, base=1, altura=1):
        self._base, self._altura = base, altura # não dá problema, pois EquiTriang é uma subclasse de Triangulo, portanto é acessível. 

class Triangulo:
    def __init__(self, base=1, altura =1):
        self.__base, self.__altura = base, altura # neste caso, se tentar acessar os atributos base e altura, irá retornar um 'erro' dizendo que eles não existem, pois são PRIVADOS.

# porém, dá pra acessar desta forma, por exemplo: t1._Triangulo__base