salario= float(input())

if salario >=0 and salario <=400:
    percentual= (0.15) 

if salario >400 and salario <=800:
    percentual= (0.12) 
    
if salario >800 and salario <=1200:
    percentual= (0.10)     
    
if salario >1200 and salario <=2000:
    percentual= (0.07)     
    
if salario >2000:
    percentual= (0.04)     
    
reajuste_ganho= salario*percentual    
novo_salario= salario+ reajuste_ganho

print('Novo salario:', f'{novo_salario:.2f}') 
print('Reajuste ganho:', f'{reajuste_ganho:.2f}') 
print('Em percentual:', int(percentual*100), '%') 