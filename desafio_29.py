total = 0
quantidade = 0

while quantidade < 2:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
        
    elif n >= 0 and n <= 10:
        quantidade = quantidade + 1
        total = total + n
        
print(f'media = {(total/2):.2f}') 