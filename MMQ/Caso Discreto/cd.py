from sympy import Symbol
from lu import lu

file_in = open('file_in.txt', 'r')
file_out = open('file_out.txt', 'w')

x = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
y = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
grau = int(file_in.readline())

matriz = []

matriz = [[j**i for j in x] for i in range(grau+1)]

def resolveMatriz(Matriz, y):
    temp = []  
    for i in range(len(matriz)):        
        temp.append(sum([y[j]*Matriz[i][j] for j in range(len(y))]))
    return temp

v = resolveMatriz(matriz, y)

def prod(matriz, x, y):
    aux = []
    for i in range(len(matriz[0])):
        aux.append(matriz[x][i] * matriz[y][i])
    return sum(aux)

def resolveMatriz(matriz):    
    temp = []  
    for i in range(len(matriz)):
            temp.append([prod(matriz, j, i) for j in range(len(matriz))])
    return temp

a = lu(len(matriz), resolveMatriz(matriz), v)
x = Symbol('x')
s = 0
for i in range(grau+1):
    s += a[i]*x**i
file_out.write("P(x) = {}" .format(s))

x = 2000
r = 1.15006680793897*x**2 - 4591.12088784926*x + 4583395.94545113
print(r)