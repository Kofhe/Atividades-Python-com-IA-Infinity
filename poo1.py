# Crie três classes separadas e independentes: Animal, Cachorro e Gato.
# Cada classe deve ter um método chamado falar (), que imprime uma mensagem específica na tela:

# - A classe Animal deve imprimir: "Este animal faz um som genérico."

# - A classe Cachorro deve imprimir: "O cachorro está latindo."

# - A classe Gato deve imprimir: "O gato está miando."

# Regras:

# - As classes não devem se relacionar entre si.

# - Cada classe deve ser criada de forma independente.

# - No final, crie um objeto para cada uma das classes e chame o método falar () de cada objeto.

class Animal: #molde animal
    def __init__(self, nome): #self objeto e nome valor
        self.nome = nome #guardando o valor dentro do objeto

    def falar(self): #metodo da classe animal (função que pertence a classe)
        print(f'Este {self.nome} faz um som genérico')

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f'O {self.nome} está latindo')

class Gato:
    def __init__(self,nome):
        self.nome = nome  

    def falar(self):
        print(f'O {self.nome} está miando')
    
animal1 = Animal("elefante")
cachorro1 = Cachorro("poodle")
gato1 = Gato("frajola")

animal1.falar()
cachorro1.falar()
gato1.falar()
