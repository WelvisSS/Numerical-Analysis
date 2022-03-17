from sympy import Symbol, simplify, expand

def interNewton(x, y, n):
    X = Symbol('x')    
    passo = 1
    tabela = [y]
    aprox = 0
    grau = 0

    for i in range(n-1):
        ordem = []
        for j in range(len(tabela[i]) - 1):
            dif_dividida = (tabela[i][j+1] - tabela[i][j])/(x[j+passo] - x[j])
            ordem.append(dif_dividida)
        tabela.append(ordem)
        passo += 1
    
    for i in range(len(tabela)):
        fator = tabela[i][0]
        for j in range(grau): fator *= (X - x[j])
        grau += 1
        aprox += fator
    
    P = simplify(aprox)
    P = expand(P)

    file_output.write(f'Px = {P}\n\n')

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

while(1):
    x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    y = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

    interNewton(x, y, len(x))
    if file_input.readline() == '': break

file_input.close()
file_output.close()