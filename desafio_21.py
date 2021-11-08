palavra0= input() 
palavra1= input() 
palavra2= input() 

animal= ''

if palavra0== 'vertebrado':
    if palavra1== 'ave':
        if palavra2== 'carnivoro':
            animal= 'aguia'
        elif palavra2== 'onivoro':
            animal= 'pomba'
    
    elif palavra1== 'mamifero':
        if palavra2== 'onivoro':
            animal= 'homem'
        elif palavra2== 'herbivoro':
            animal= 'vaca'
            
if palavra0== 'invertebrado':
    if palavra1== 'inseto':
        if palavra2== 'hematofago':
            animal= 'pulga'
        elif palavra2== 'herbivoro':
            animal= 'lagarta' 
            
    elif palavra1== 'anelideo':
        if palavra2== 'onivoro':
            animal= 'minhoca'
        elif palavra2== 'hematofago':
            animal= 'sanguessuga'

print(animal)  