from math import e
def funcao (func, x, y): return eval(func)

def heun (func, x, y, h, inter):
    i = 1
    k = 0
    it = 0       
    while(x[k] < inter[1]):        
        y.append(y[i-1] + h*(funcao(func, x[k], y[i-1])))
        y[i] = y[i - 1] + (h/2)*(funcao(func, x[k], y[i-1]) + funcao(func, x[k]+h, y[i]))
        x.append(x[k] + h)
        i = i + 1
        k = k + 1
        it += 1
    file_out.write("Função utilizada: {}" .format(func))
    file_out.write("Iterações de X: {}\n" .format(x))
    file_out.write("Iterações de Y: {}\n" .format(y))
    file_out.write("Y({}) = {}\n" .format(inter[1], y[-1]))
    file_out.write("Número de Iterações: {}\n\n" .format(it))
# Heun para sistemas de equações diferenciais
def func(f, x, y, z): return eval(f)

def heunS(f, x, y, z, h, inter):
    it = 0
    for i in range(int(inter[1]/h)):
        k1 = [func(f[0], x[i], y[i], z[i]), func(f[1], x[i], y[i], z[i])]
        x.append(x[i]+h)
        y.append(y[i]+h*k1[0])
        z.append(z[i]+h*k1[1])
        k2 = [func(f[0], x[i], y[i], z[i+1]), func(f[1], x[i+1], y[i+1], z[i])]
        s = [y[i]+(h/2)*(k1[0]+k2[0]), z[i]+(h/2)*(k1[1]+k2[1])]
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
    f = file_in.readline()
    if f[0] == '$':
        f = f.replace('$', '').replace('\n', '').split('|')
        yz = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        h = float(file_in.readline())
        intervalo = [0, float(file_in.readline())]
        heunS(f, [0], [yz[0]], [yz[1]], h, intervalo)
    else:
        intervalo = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        x = [intervalo[0]] # x inicial
        h = float(file_in.readline())
        y = [float(file_in.readline())] # y inicial
        heun(f, x, y, h, intervalo)

    if(file_in.readline() == ""): break