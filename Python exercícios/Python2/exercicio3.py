populacaoBrasil = float(input('Insira a população do Brasil: '))
populacaoChina = float(input('Insira a população da China: '))

if populacaoBrasil < populacaoChina:
    print('A população da China é maior.')

elif populacaoBrasil > populacaoChina:
    print('A população do Brasil é maior.')

else: 
    print('As duas naçoes tem a mesma população')