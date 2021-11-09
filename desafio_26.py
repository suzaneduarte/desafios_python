data_i= input().split(' ')[1]
data_i= int(data_i)
hora_i, minuto_i, segundo_i = list(map(int, input().split(':')))
data_f= input().split(' ')[1]
data_f= int(data_f)
hora_f, minuto_f, segundo_f = list(map(int, input().split(':')))

tempo_inicial= (data_i*24*3600)+(hora_i*3600)+(minuto_i*60)+segundo_i
tempo_final= (data_f*24*3600)+(hora_f*3600)+(minuto_f*60)+segundo_f
horario= tempo_final-tempo_inicial 

print(f'{(horario//(3600*24))} dia(s)')
horario = horario - (horario//(3600*24))*3600*24
print(f'{(horario//3600)} hora(s)')
horario = horario - (horario//(3600))*3600
print(f'{(horario//60)} minuto(s)')
print(f'{(horario%60)} segundo(s)')