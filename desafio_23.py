salario= float(input()) 
imposto= 0
    
if salario>2000 and salario <=3000: 
    imposto= (salario - 2000)*0.08
    
elif salario>3000 and salario <=4500: 
    imposto= 1000*0.08 
    imposto= imposto + (salario-3000)*0.18
    
elif salario>4500:
    imposto= 1000*0.08 
    imposto= imposto + 1500*0.18
    imposto= imposto + (salario-4500)*0.28

if imposto==0: 
    print('Isento')
    
else: 
    print('R$', f'{imposto:.2f}')
