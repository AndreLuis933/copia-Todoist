from abc import ABC, abstractmethod

# Abstração: Definição de um contrato
class MeioDeTransporte(ABC):
    @abstractmethod
    def mover(self):
        pass

# Implementações concretas
class Carro(MeioDeTransporte):
    def mover(self):
        print("Dirigindo na estrada.")

class Bicicleta(MeioDeTransporte):
    def mover(self):
        print("Pedalando na ciclovia.")

class Aviao(MeioDeTransporte):
    def mover(self):
        print("Voando pelo céu.")

# Função que utiliza a abstração
# Ela não se preocupa com o tipo específico de transporte, apenas com o contrato (mover)
def iniciar_jornada(transporte: MeioDeTransporte):
    transporte.mover()

# Exemplo de uso
if __name__ == "__main__":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    

