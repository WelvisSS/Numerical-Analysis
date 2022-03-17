from math import e
def formula(func, x, y): return eval(func)

def euler (func, x, y, h, inter):
    i = 1
    k = 0    
    it = 0   
    while(x[k] < inter[1]):        
        y.append(y[i-1] + h*(formula(func, x[k], y[i-1])))
        x.append(x[k] + h)
        i += 1
        k += 1
        it += 1
    file_out.write("Função utilizada: {}" .format(func))
    file_out.write("Iterações de X: {}\n" .format(x))
    file_out.write("Iterações de Y: {}\n" .format(y))
    file_out.write("Y({}) = {}\n" .format(inter[1], y[-1]))
    file_out.write("Número de Iterações: {}\n\n" .format(it))
# Euler para sistemas de equações diferenciais
def func(f, x, y, z): return eval(f)

def eulerS(f, inter, h, x, y, z):
    i = 0    
    k = 0
    it = 0
    for i in range(int(inter[1]/h)):        
        s = [y[i], z[i]]
        m = [h*func(f[0], x[i], y[i], z[i]), h*func(f[1], x[i], y[i], z[i])]
        r = [s[j]+m[j] for j in range(len(s))]
        x.append(x[0]+h)
        y.append(r[0])
        z.append(r[1])
        i += 1
        k += 1
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
        eulerS(funcao, intervalo, h, [0], [yz[0]], [yz[1]])
    else:
        intervalo = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        h = float(file_in.readline())
        y = [float(file_in.readline())]
        euler (funcao, [0], y, h, intervalo)

    if(file_in.readline() == ""): break