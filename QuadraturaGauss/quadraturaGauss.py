from math import e, pi, sqrt
tabela = open('tabela.txt', 'r')
file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')

func = file_in.readline().replace('\n', '')
intervalo = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
n_tabela = int(tabela.readline())
tab = []

for i in range(n_tabela):
    tab.append([float(j) for j in tabela.readline().replace('\n', '').split(' ')])

def f(x):
    global func
    return eval(func)

def quadratura(f, p):
    soma = 0
    for c, x in p: soma += c * f(x)
    return soma

def mudanca(f, a, b, u):
    return f((b+a)/2 + (b-a)*u/2) * (b-a)/2

a, b = intervalo

def g(u): return mudanca(f, a, b, u)

I = quadratura(g, tab)

file_out.write("I: {}\n\n" .format(I))

tabela.close()
file_in.close()
file_out.close()