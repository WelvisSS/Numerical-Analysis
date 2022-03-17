def funcao(x, f): return eval(f)

def Ordem1 (func, x, h) :
    x_retardada = (funcao(x, func) - funcao(x-h, func))/(h)
    x_centrada = (funcao(x+h, func) - funcao(x-h, func))/(2*h)
    x_avancada = (funcao(x+h, func) - funcao(x, func))/(h)
    file_output.write("Retardada = {}\n" .format(x_retardada))
    file_output.write("Centrada = {}\n" .format(x_centrada))
    file_output.write("Avancada = {}\n\n" .format(x_avancada))

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

while(1):
    func = file_input.readline()
    x = int(file_input.readline())
    h = float(file_input.readline())
    Ordem1(func, x, h)
    if file_input.readline() == '': break

file_input.close()
file_output.close()