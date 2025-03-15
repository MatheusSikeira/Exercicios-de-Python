numero1 = int(input('Insira o primeiro valor: '))
numero2 = int(input('Insira o segundo valor: '))
numero3 = int(input('Insira o terceiro valor: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'o maior numero é {numero1}')

elif numero1 < numero3 and numero2 < numero3:
    print(f'o maior numero é {numero3}')

elif numero2 > numero3 and numero2 > numero1:
    print(f'o maior numero é {numero2}')

else:
    print(f'Os numeros são iguais')