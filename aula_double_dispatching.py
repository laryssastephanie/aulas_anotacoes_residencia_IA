# Double Dispatching = criar um segundo nível para a operação ser executada
# Pedir para um objeto que ele se compare com o outro

class FormaGeometrica:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Circulo(FormaGeometrica):
    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.raio = raio

    def compara_quadrado(self, quadrado):
        return False # circulo se compara com quadrado e retorna FALSE

    def compara_circulo(self, outro_circulo):
        return self.x == outro_circulo.x and self.y == outro_circulo.y and self.raio == outro_circulo.raio

    def __eq__(self, outro):
        return outro.compara_circulo(self) # tipo de self já é circulo. Então delegamos para o 'outro' dar a resposta dessa comparação


class Quadrado(FormaGeometrica):
    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def compara_circulo(self, circulo): 
        return False # como se perguntasse ao quadrado para ele se compara com o circulo = ele responde FALSE

    def compara_quadrado(self, outro_quadrado):
        return self.x == outro_quadrado.x and self.y == outro_quadrado.y and self.lado == outro_quadrado.lado

    def __eq__(self, outro):
        return outro.compara_quadrado(self)
    

class Quadro:
    formas_geometricas = []

    def adicionar_forma(self, forma):
        Quadro.formas_geometricas.append(forma)

    def remover_forma_em(self, index=0):
        Quadro.formas_geometricas.pop(index)

    def remover_forma(self, forma):
        for i, f in enumerate(Quadro.formas_geometricas):
            if(f == forma): # precisa escrever o método "eq" para que este operador de igualdade funcione
                self.remover_forma_em(i)
                break

c1 = Circulo(10, 20, 5)
c2 = Circulo(10, 20, 5)
c3 = Circulo(10, 30, 5)

q1 = Quadrado(10, 20, 5)
q2 = Quadrado(10, 20, 5)
q3 = Quadrado(10, 30, 5)

quadro = Quadro()

quadro.adicionar_forma(c1)
quadro.adicionar_forma(c2)
quadro.adicionar_forma(c3)
quadro.adicionar_forma(q1)
quadro.adicionar_forma(q2)
quadro.adicionar_forma(q3)

print(len(Quadro.formas_geometricas))
print("Removendo a última forma")
quadro.remover_forma_em(5)
print(len(Quadro.formas_geometricas))

c4 = Circulo(10, 30, 5)

print(f"C3 == c4: {c3 == c4}")
print(f"Q3 == C4: {q3 == c4}")

quadro.remover_forma(c4) # c4 nao está dentro da lista, mas é igual ao c3

print(len(quadro.formas_geometricas))

