N1,N2,N3,N4= input().split(' ')

N1= float(N1)
N2= float(N2)
N3= float(N3)
N4= float(N4)

media= (2*N1+ 3*N2 + 4*N3 + 1*N4)/10

print('Media:', f'{(media):.1f}')

if media>=7.0: 
    print('Aluno aprovado.')
    
elif media<5.0:
    print('Aluno reprovado.')
    
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame:', f'{(nota_exame):.1f}')
    nova_media = (nota_exame + media)/2
    if nova_media>=5.0: 
        print('Aluno aprovado.')
        print('Media final:', f'{(nova_media):.1f}')
    else: 
        print('Aluno reprovado.')
        print('Media final:', f'{(nova_media):.1f}')