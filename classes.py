class Animal:
    def __init__(self, tipo, peso, alimentacao):
        self.tipo = tipo
        self.peso = peso
        self.alimentacao = alimentacao
    
    def apresentacao_animal(self):
        return f'Sou um(a) {self.tipo}, tenho {self.peso} kg e sou {self.alimentacao}'


class Humano(Animal):
    def __init__(self, nacionalidade):
        super()
        self.__nacionalidade = nacionalidade
    
    def pais_origem(self):
        if self.__nacionalidade == 'Brasil':
            return f'Sou uma {self.tipo}, que tem {self.peso}kg e sou brasileira.'


pessoa = Humano("Pessoa", 68, 'carnívora', 'Brasil')
print(pessoa.pais_origem())