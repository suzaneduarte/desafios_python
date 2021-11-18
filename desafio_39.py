N = int(input())

for i in range(N):
	texto = input().split(" ")
	texto2 = []
	texto3 = []
	for x in texto:
		if x != "":
			texto2.append(x)

	for y in texto2:
		texto3.append(y[0])
	print(''.join(texto3))