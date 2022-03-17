from math import e, pi

def f(fun, x):
    return eval(fun)

def simpson13(pontos, fun):
    h = (pontos[-1] - pontos[0])
    I = h*((f(fun, pontos[0]) + 4*f(fun, h/2) + f(fun, pontos[-1]))/6)
    file_output.write(f'I = {I}')

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

func = file_input.readline()
pontos = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
n = int(file_input.readline())

simpson13(pontos, func)
file_input.close()
file_output.close()

