class Pet:
    def __init__(self,nome,idade,cor,raca):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca 

    def analisaidade(self):
        while True:
            try:
                idade = int(input("Digite a idade de seu pet: "))
                if 1 == idade <= 100:
                    print(f"Seu tem {idade} anos")
                    break
                else:
                    print("Idade inválida")
            except ValueError:
                print("Entrada inválida")
                
    def analisanome(self):
        while True:
            try:
                nome = input()
                break
            
            except 
        