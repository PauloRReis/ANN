matriz = [[1/3, -7/9], [8/9, -1/4], [2/3,-2]]

vet = []
for i in range(len(matriz[2])):
    vet.append(-3.03*matriz[1][i])

for i in range(len(matriz[2])):
    matriz[0][i] += vet[i]

aux = matriz[1]
matriz[1] = matriz[0]
matriz[0] = aux

aux = matriz[2]
matriz[2] = matriz[0]
matriz[0] = aux

vet1 = []
for i in range(len(matriz[2])):
    vet1.append(-0.88*matriz[0][i])

for i in range(len(matriz[2])):
    matriz[1][i] += vet1[i]

for i in range(len(matriz[1])):
    matriz[2][i] *= -1.27

print(matriz)

""" aux = matriz[0]
matriz[0] = matriz[1]
matriz[1] = aux

for i in range(len(matriz[1])):
    matriz[0][i] *= -4.91

vet = []
for i in range(len(matriz[1])):
    vet.append(1.0*matriz[1][i])

for i in range(len(matriz[2])):
    matriz[2][i] += vet[i]
 """
""" vet = []
for i in range(len(matriz[1])):
    vet.append(4.32*matriz[1][i])

for i in range(len(matriz[2])):
    matriz[2][i] += vet[i]

for i in range(len(matriz[1])):
    matriz[1][i] *= 3.38

aux = matriz[0]
matriz[0] = matriz[1]
matriz[1] = aux """


""" for i in range(len.natriz[1]):
    aux = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = matriz[i] """

""" for i in range(len(matriz)):
    for j in range(len(matriz[i])): """
        
#[[-9.9182, 16.8904, -12.569600000000001], [3.17, 2.22, -4.85], [5.24, 0.03000000000000025, -6.4799999999999995]]





