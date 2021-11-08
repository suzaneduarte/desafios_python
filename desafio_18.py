inicial,final= input().split(' ')
inicial= int(inicial)
final= int(final)

tempo= final-inicial 

if tempo<=0:
    tempo= (final-inicial)+24
    
print(f'O JOGO DUROU {tempo} HORA(S)') 