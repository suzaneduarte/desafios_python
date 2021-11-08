h_inicial,m_inicial,h_final,m_final= input().split(' ')
h_inicial= int(h_inicial)
m_inicial= int(m_inicial)
h_final= int(h_final)
m_final= int(m_final)

tempo_inicial= (h_inicial*60)+ m_inicial 
tempo_final= (h_final*60)+ m_final 
tempo= tempo_final-tempo_inicial 

if tempo<=0:
    tempo= (tempo_final-tempo_inicial)+24*60 
    
print(f'O JOGO DUROU {(tempo//60)} HORA(S) E {(tempo%60)} MINUTO(S)')