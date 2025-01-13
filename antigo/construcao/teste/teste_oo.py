

class Gato():
    nome = "tigre"
    cor = "branco"
    def __init__(self):
        self.cor = "preto"
    
    def eat(self):
        return"comendo"
    
    def get_cor(self):
        return self.cor
    

gato = Gato()

print(gato.nome)
print(gato.eat())
print(gato.get_cor())