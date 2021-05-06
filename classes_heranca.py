import math

class FormaGeometrica:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def desenhe(self):
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})" + "\n")

f1 = FormaGeometrica(0, 0)
f1.desenhe()

class Forma2D(FormaGeometrica):
    def __init__(self, x, y):
        super().__init__(x, y)


f1_2D = Forma2D(0, 0)
f1_2D.desenhe()

class Forma3D(FormaGeometrica):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        

f1_3D = Forma3D(0, 0, 0)
f1_3D.desenhe()


class Poligono(Forma2D):
    def __init__(self, x, y, quantidade_lados, tamanho_lados, apotema):
        super().__init__(x, y)
        self.quantidade_lados = quantidade_lados
        self.tamanho_lados = tamanho_lados
        self.apotema = apotema
    def desenhe(self):
        perimetro = self.quantidade_lados * self.tamanho_lados
        area = (perimetro * self.apotema) / 2
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})")
        print("O perímetro do Polígono é " + str(perimetro))
        print("A área do Polígono é " + str(area) + "\n")

pol_2D = Poligono(0, 0, 5, 2, 1)
pol_2D.desenhe()

class Retangulo(Forma2D):
    def __init__(self, x, y, altura, largura):
        super().__init__(x, y)
        self.altura = altura
        self.largura = largura
    def desenhe(self):
        area = self.altura * self.largura
        perimetro = 2 * (self.altura + self.largura)
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})")
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area) + "\n")


ret_2D = Retangulo(0, 0, 2, 5)
ret_2D.desenhe()

class Quadrado(Retangulo):
    def __init__(self, x, y, altura, largura):
        super().__init__(x, y, altura, largura)

qd_2D = Quadrado(0, 0, 4, 4)
qd_2D.desenhe()

class Esfera(Forma3D):
    def __init__(self, x, y, z, raio):
        super().__init__(x, y, z)
        self.raio = raio
    def desenhe(self):
        area = 4 * math.pi * (self.raio ** 2)
        perimetro = 2 * math.pi * self.raio
        volume = (4 * math.pi * (self.raio ** 3)) / 3
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})")
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area))
        print(f"O volume do {type(self).__name__} é " + str(volume) + "\n")

esf = Esfera(0, 0, 0, 5)
esf.desenhe()

class Cubo(Forma3D):
    def __init__(self, x, y, z, aresta):
        super().__init__(x, y, z)
        self.aresta = aresta
    def desenhe(self):
        area = 6 * self.aresta ** 2
        perimetro = 12 * self.aresta
        volume = self.aresta ** 3
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})")
        print(f"O perímetro do {type(self).__name__} é " + str(perimetro))
        print(f"A área do {type(self).__name__} é " + str(area))
        print(f"O volume do {type(self).__name__} é " + str(volume) + "\n")

cb = Cubo(0, 0, 0, 2)
cb.desenhe()

class Cilindro(Forma3D):
    def __init__(self, x, y, z, raio, altura):
        super().__init__(x, y, z)
        self.raio = raio
        self.altura = altura
    def desenhe(self):
        areaBase = math.pi * (self.raio ** 2)
        areaLateral = 2 * math.pi * self.altura * self.raio
        areaTotal = (2 * areaBase) + areaLateral
        volume = areaBase * self.altura
        print(f"{type(self).__name__} centrada(o) em ({self.x}, {self.y})")
        print(f"A área do {type(self).__name__} é " + str(areaTotal))
        print(f"O volume do {type(self).__name__} é " + str(volume) + "\n")

cl = Cilindro(0, 0, 0, 3, 5)
cl.desenhe()


class Quadro:
    def __init__(self):
        self.figuras_geometricas = []
    