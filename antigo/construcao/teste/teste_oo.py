

class Gato():
    def __init__(self):
        self.cor = "branco"
        self.nome = "tigre"
    
    def eat(self):
        return"comendo"
    
    def get_cor(self):
        return self.cor
    

gato = Gato()

print(gato.nome)
print(gato.eat())
print(gato.get_cor())