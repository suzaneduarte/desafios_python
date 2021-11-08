valores= input()
codigo,quantidade= valores.split(' ')

codigo= int(codigo)
quantidade= int(quantidade)

if codigo == 1:
    preço=4.00
    
if codigo == 2:
    preço=4.50
    
if codigo == 3:
    preço=5.00
    
if codigo == 4:
    preço=2.00
    
if codigo == 5:
    preço=1.50  

total= quantidade*preço 
print('Total: R$', f'{(total):.2f}') 