from sympy import Symbol, sympify, integrate
def matrizes (grau, inter_a, inter_b, func):
    x = Symbol('x')
    for col in range(grau+1):
        linha = [0.0] * (grau+1)
        for lin in range(grau+1):
            linha[lin] = integrate(((x**lin) * (x**col)), (x, inter_a, inter_b))
        Matriz_f[col] = integrate((sympify(func) * (x**col)), (x, inter_a, inter_b))
        Matriz_k.append(linha)

def triangulacao(grau, Matriz_k, Matriz_f):    
    for k in range(grau+1):
        if k == grau-1: k = k - 1
        for i in range(k+1, grau+1):
            m = Matriz_k[i][k] / Matriz_k[k][k]
            Matriz_k[i][k] = 0
            for j in range(k+1, grau+1):
                Matriz_k[i][j] = Matriz_k[i][j] - (m * Matriz_k[k][j])
            
            Matriz_f[i] = Matriz_f[i] - (m * Matriz_f[k])

def solucao(grau, Matriz_k, Matriz_f, func):
    matrizes (grau, inter_a, inter_b, func)
    triangulacao(grau, Matriz_k, Matriz_f)
    X = [0.0] * (grau+1)
    X[grau] = Matriz_f[grau] / Matriz_k[grau][grau]
    for i in range(grau, -1, -1):
        s = 0.0
        for j in range(i+1, grau+1):
            s = s + (Matriz_k[i][j] * X[j])
            X[i] = (Matriz_f[i] - s) / Matriz_k[i][i] 
            
    return X


file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
func = file_in.readline()
inter_a = int(file_in.readline())
inter_b = int(file_in.readline())
grau = int(file_in.readline())
Matriz_k = []
Matriz_f = [0.0] * (grau+1)
a = solucao(grau, Matriz_k, Matriz_f, func)
x = Symbol('x')
soma = 0
for i in range(grau+1):
    soma = soma + a[i]*x**i
file_out.write("P(x) = {}" .format(soma))
