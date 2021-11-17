input()
lista= list(map(int, input().split()))
minimo_global= min(lista)
indice= lista.index(minimo_global)

print(f'Menor valor: {minimo_global}')        
print(f'Posicao: {indice}')