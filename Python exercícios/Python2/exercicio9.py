peso = float(input('Informe seu peso: ').replace(',', '.'))

altura = float(input('Informe sua altura: ').replace(',', '.'))

formula = peso / (altura * altura)

if formula <= 16.9:
    print(f'{formula:.2f} Muito abaixo do peso')
    
elif formula <= 18.9:
    print(f'{formula:.2f} Abaixo do peso')
    
elif formula <= 26.9:
    print(f'{formula:.2f} Normal') 
    
elif formula <= 31.9:
    print(f'{formula:.2f} Acima do peso')
    
else:
    print(f'{formula:.2f} Obsidade')