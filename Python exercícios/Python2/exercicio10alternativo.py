while True:
    try:
        nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))

        if 0 <= nota1 <= 10:
            print(f'Valor válido: {nota1}')
            break
        else:

            print('O valor deve estar entre 0 e 10.')

    except ValueError:
            print('Entrada inválida, por favor, digite apenas números')
        
while True:
    try:
        nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))

        if 0 <= nota2 <= 10:
            print(f'Valor válido: {nota2}')
            break
        else:

            print('O valor deve estar entre 0 e 10.')

    except ValueError:
            print('Entrada inválida, por favor, digite apenas números')
            
while True:
    try:
        nota3 = float(input('Digite a terceira nota: ').replace(',', '.'))

        if 0 <= nota3 <= 10:
            print(f'Valor válido: {nota3}')
            break
        else:

            print('O valor deve estar entre 0 e 10.')

    except ValueError:
            print('Entrada inválida, por favor, digite apenas números')
            
while True:
    try:
        nota4 = float(input('Digite a quarta nota: ').replace(',', '.'))

        if 0 <= nota4 <= 10:
            print(f'Valor válido: {nota4}')
            break
        else:

            print('O valor deve estar entre 0 e 10.')

    except ValueError:
            print('Entrada inválida, por favor, digite apenas números')
            
    

media = (nota1 + nota2 + nota3 + nota4) / 4



if media >= 7:
    print(f'{media:.2f} Aluno aprovado')
    
elif media <= 6.9:
    print(f'{media:.2f} Aluno está de recuperação') 
    
else:
    print(f'{media:.2f} Aluno reprovao') 