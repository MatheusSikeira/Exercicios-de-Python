class Exemplo:
    variavel_de_classe = 0 # variavel de classe
    def __init__(self):
        Exemplo.variavel_de_classe += 1
a = Exemplo()
b = Exemplo()
C = Exemplo()
print(Exemplo.variavel_de_classe) # saída 2 pois exemplo recebe duas vezes o += 1
        