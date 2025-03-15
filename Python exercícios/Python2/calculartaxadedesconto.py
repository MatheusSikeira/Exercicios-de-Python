valorF = float(input('Digite o valor futuro: '))
taxaD = float(input('Digite a taxe de desconto: '))
tempo = float(input('Digite o tempo: '))

PV = valorF / (1 + (taxaD*tempo))
print(f'A taxa de desconto é de {}')

