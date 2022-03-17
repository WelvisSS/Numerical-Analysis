from math import e, pi, sqrt
def f(fun, x):
    return eval(fun)

def simpson38(pontos, fun, n):
    h = (pontos[-1] - pontos[0])
    integration = 0
    p = [pontos[0]+(h/n)]
    
    for i in range(1, n-1): p.append(p[i-1]+(h/n))
    
    for i in p: integration += 3 * f(fun, i)

    I = h*((f(fun, pontos[0]) + integration + f(fun, pontos[-1]))/8)
    file_output.write(f'I = {I}\n\n')

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')
while(1):
    func = file_input.readline()
    pontos = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    n = int(file_input.readline())
    simpson38(pontos, func, n)
    if file_input.readline() == '': break
file_input.close()
file_output.close()