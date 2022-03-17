from sympy import Symbol, simplify, expand
import numpy as np
import matplotlib.pyplot as mp

def lagrange (x, y, n):
    X = Symbol('x')
    l = []
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j: L *= (X - x[j])/(x[i] - x[j])
        l.append(L)
    s = 0    
    for i in range(len(l)): s += y[i]*l[i]
        
    P = simplify(s)
    P = expand(P)
    
    funcao = lambda x: eval(str(P))
    res = [funcao(ponto) for ponto in x]
    mp.plot(x, y, 'bo')
    mp.plot(x, res)

    mp.show()

    file_output.write("Px = {}\n\n" .format(P))

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')


x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

y = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

lagrange(x, y, len(x))

    

file_input.close()
file_output.close()

