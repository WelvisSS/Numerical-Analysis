def k1 (func, x, y): return eval(func)

def k2 (func, x, h, y):
    x1 = (3/4)*h + x
    y1 = y + (3/4)*h*(k1(func, x, y))
    return (k1(func, x1, y1))
    
def ralston (func, x, h, inter):
    i = 1
    k = 0    
    it = 0
    while(x[k] < inter[1]):        
        y.append(y[i-1] + (((1/3)*k1(func, x[k], y[i-1])) + ((2/3)*(k2(func, x[k], h, y[i-1]))))*h)
        x.append(x[k] + h)
        i += 1
        k += 1
        it += 1
    file_out.write("Função utilizada: {}" .format(func))
    file_out.write("Iterações de X: {}\n" .format(x))
    file_out.write("Iterações de Y: {}\n" .format(y))
    file_out.write("Y({}) = {}\n" .format(inter[1], y[-1]))
    file_out.write("Número de Iterações: {}\n\n" .format(it))

# Ralston para sistema de equações diferenciais
def ralstonS(f, f1, f2, x, y, z, h, inter):
    it = 0
    for i in range(int(inter[1]/h)):
        k1, k2 = [None, None], [None, None]
        k1[0] = f1(x[i], y[i], z[i])
        k1[1] = f2(x[i], y[i], z[i])
        k2[0] = f1(x[i]+(3/4)*h, y[i], z[i] + (3/4)*k1[1]*h)
        k2[1] = f2(x[i]+(3/4)*h, y[i] + (3/4)*k1[0]*h, z[i])
        y1 = y[i] + ((((1/3) * k1[0]) + ((2/3) * k2[0])) * h)
        z1 = z[i] + ((((1/3) * k1[1]) + ((2/3) * k2[1])) * h)
        x.append(x[i]+h), y.append(y1), z.append(z1)
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
        y = [yz[0]]
        z = [yz[1]]
        x = [0]
        f1 = lambda x, y, z: eval(funcao[0])
        f2 = lambda x, y, z: eval(funcao[1])
        ralstonS(funcao, f1, f2, x, y, z, h, intervalo)
    else:
        intervalo = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
        x = [intervalo[0]]
        h = float(file_in.readline())
        y = [float(file_in.readline())]
        ralston(funcao, x, h, intervalo)

    if(file_in.readline() == ""): break