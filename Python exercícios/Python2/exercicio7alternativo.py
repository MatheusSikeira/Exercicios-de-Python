entrada = input('Digite três números separados por vírgulas: ')

valores_string = entrada.split(',')

if len(valores_string) != 3:
    print('Erro você não forneceu três valores')

else: 
    try:
        valores = [int(valor) for valor in valores_string]
        print(f'Valores recebidos: {valores}')

    except ValueError:
        print(f'Erro todos os valores devem ser inteiros')