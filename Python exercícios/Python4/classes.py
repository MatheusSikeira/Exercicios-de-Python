class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
            print(f"{self.nome} está latindo")

#criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex", 5)
print(meu_cachorro.nome) #acessando o atributo 'nome'
print(meu_cachorro.idade) #acessando o atributo idade
meu_cachorro.latir() #Chamando o método 'latir'