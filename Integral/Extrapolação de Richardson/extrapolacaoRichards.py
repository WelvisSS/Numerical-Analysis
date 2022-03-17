from math import e, pi, sqrt

def funcao(f, x):
    return eval(f)

def trapezioSimples(x0, func):
    h = x0[-1] - x0[0] 
    I = h*((funcao(func, x0[0]) + funcao(func, x0[-1]))/2)
    return I

def trapezioMultiplo(x0, func):
    n = len(x0)
    Somatorio = sum(funcao(func, x0[i]) for i in range(1, n-1))  
    h = x0[-1] - x0[0]  
    I = h*((funcao(func, x0[0]) + 2*Somatorio + funcao(func, x0[-1]))/(2*(n-1)))
    return I

def richards(x0, func):
    I1 = trapezioSimples(x0, func)
    I2 = trapezioMultiplo(x0[::2], func)
    I3 = trapezioMultiplo(x0, func)

    I4 = 4/3*(I2)- 1/3*(I1)
    I5 = 4/3*(I3)- 1/3*(I2)
    I = 16/15*(I5)- 1/15*(I4)

    return I


file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')
while(1):
    func = file_input.readline().replace('\n', '')
    x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    t = int(file_input.readline().replace('\n', ''))
    h = (x[1] - x[0])/t

    pontos = [x[0]]
    for i in range(1, t+1): pontos.append(pontos[i-1]+h)

    file_output.write("I = {}\n\n".format(str(richards(pontos, func))))
    if file_input.readline() == '': break
file_input.close()
file_output.close()