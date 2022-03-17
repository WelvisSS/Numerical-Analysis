from math import e
def k1 (func, x, y): return eval(func)

def k2 (func, x, h, y):
    x1 = x + (1/2)*h
    y1 = y + (1/2)*h*(k1(func, x, y))
    return (k1(func, x1, y1))

def k3 (func, x, y, h):
    x1 = x + (1/2)*h
    y1 = y + (1/2)*(k2(func, x, h, y))*h
    return (k1(func, x1, y1))

def k4 (func, x, y, h):
    x1 = x + h
    y1 = y + k3(func, x, y, h)*h
    return (k1(func, x1, y1))

def quarta (f, x, y, h, inter):
    i = 1
    k = 0
    it = 0
    while(x[k] < inter[1]):
        y.append(y[i-1] + (1/6)*(k1(f, x[k], y[i-1]) + 2*(k2(f, x[k], h, y[i-1])) + 2*k3(f, x[k], y[i-1], h) + k4(f, x[k], y[i-1], h))*h)
        x.append(x[k] + h)
        i += 1
        k += 1
        it += 1

    file_out.write("Função utilizada: {}" .format(f))
    file_out.write("Iterações de X: {}\n" .format(x))
    file_out.write("Iterações de Y: {}\n" .format(y))
    file_out.write("Y({}) = {}\n" .format(inter[1], y[-1]))
    file_out.write("Número de Iterações: {}\n\n" .format(it))
#Runge Kutta para sistemas de equações diferenciais
def func(f, x, y, z): return eval(f)

def rungeKutta4S(f, x, y, z, h, inter):
    it = 0
    for i in range(int(inter[1]/h)):
        k1 = [func(f[0], x[i], y[i], z[i]), func(f[1], x[i], y[i], z[i])]
        x.append(x[i]+h/2)
        y.append(y[i]+(h/2)*k1[0])
        z.append(z[i]+(h/2)*k1[1])
        k2 = [func(f[0], x[i], y[i], z[i+1]), func(f[1], x[i+1], y[i+1], z[i])]
        y[i+1] = y[i]+(h/2)*k2[0]
        z[i+1] = z[i]+(h/2)*k2[1]
        k3 = [func(f[0], x[i], y[i], z[i+1]), func(f[1], x[i+1], y[i+1], z[i])]
        x[i+1] = x[i]+h
        y[i+1] = y[i]+(h)*k3[0]
        z[i+1] = z[i]+(h)*k3[1]
        k4 = [func(f[0], x[i], y[i], z[i+1]), func(f[1], x[i+1], y[i+1], z[i])]
        s = [y[i]+(h/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), z[i]+(h/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]
        y[i+1] = s[0]
        z[i+1] = s[1]
        it += 1

    file_out.write("Funções utilizadas: {}\n" .format(f))
    file_out.write("Iterações de Y: {}\n" .format(y))
    file_out.write("Iterações de Z: {}\n" .format(z))
    file_out.write("Y = {}\nZ = {}\n" .format(y[-1], z[-1]))
    file_out.write("Iterações: {}\n\n" .format(it))

file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
while(True):
    funcao = file_in.readline()
    if funcao[0] == '$':
        funcao = funcao.replace('$', '').replace('\n', '').split('|')
        yz = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        h = float(file_in.readline())
        intervalo = [0, float(file_in.readline())]
        rungeKutta4S(funcao, [0], [yz[0]], [yz[1]], h, intervalo)
        if(file_in.readline() == ""): break
    else:
        intervalo = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        x = [intervalo[0]]
        h = float(file_in.readline())
        y = [float(file_in.readline())]
        quarta(funcao, x, y, h, intervalo)
        if(file_in.readline() == ""): break