from math import e
def shooting(func, f1, f2, chute, h, valor, yt, y0, pontos):
    it = 0
    for j in range(3):
        x = [0]
        y = [y0]
        if j != 2:
            z = [chute[j]]
            for i in range(pontos):        
                y.append(y[i]+h*f1(x[i], y[i], z[i]))
                z.append(z[i]+h*f2(x[i], y[i], z[i]))
                x.append(x[i]+h)
                it += 1
            yt.append(y[-1])

            if y[-1] == valor: break
        else:
            z = [chute[0]+((chute[1]-chute[0])/(yt[1]-yt[0]))*(valor-yt[0])]
            for i in range(pontos):
                y.append(y[i]+h*f1(x[i], y[i], z[i]))
                z.append(z[i]+h*f2(x[i], y[i], z[i]))
                x.append(x[i]+h)
                it += 1
    file_out.write("Função = {}" .format(func))
    file_out.write("X = {}\n" .format(x))
    file_out.write("Y = {}\n" .format(y))
    file_out.write("Z = {}\n" .format(z))
    file_out.write("Z({}) = {}\nZ({}) = {}\n" .format(chute[0], yt[0], chute[1], yt[1]))
    file_out.write("Z(0) = {}\nY = {}\n" .format(z[0], y[-1]))
    file_out.write("Iterações = {}\n\n" .format(it))

file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
while(True):
    func = file_in.readline()
    chute = [float(i) for i in file_in.readline().replace('\n', '').split(' ')]
    h = float(file_in.readline())
    valor = float(file_in.readline())
    y0 = float(file_in.readline())
    pontos = int(file_in.readline())
    f1 = lambda x,y,z: z
    f2 = lambda x,y,z: eval(func)
    shooting(func, f1, f2, chute, h, valor, [], y0, pontos)
    if(file_in.readline() == ""): break