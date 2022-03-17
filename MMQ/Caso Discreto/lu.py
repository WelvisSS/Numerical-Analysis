# Diferente da triangulação feita no método de Gauss, esse 
# método além de criar uma matriz U com valores abaixo da  
# diagonal principal zerados, também cria a matriz L com 
# valores da diagonal principal e acima dela preenchidos.
I = []

def matriz_LU (size, A):
    for k in range(size):
        for i in range(k+1, size):
            # Calculandno o multiplicador da linha
            m = A[i][k] / A[k][k]
            # Zerando valores abaixo da diagonal principal.
            A[i][k] = 0.0            
            # Fzendo a substituição dos valores abaixo da 
            # diagonal principal da matriz L, pelos resultados 
            # obtidos em m que é o multiplicador da linha em questão.
            I[i][k] = m             
            # Preenchendo a matriz U na diagonal principal 
            # e acima dela com seus respectivos valores.
            for j in range(k+1, size):
                # Definindo o volar da posição j de cada linha.
                A[i][j] = A[i][j] - (m * A[k][j])
    
    return A
# Verifica se para cada coluna o pivo é diferente de zero.
# Verifica também se o pivo é o maior número da sua coluna.
# Caso o pivô não seja o maior da sua coluna, é feita a 
# troca com o maior.
def pivo (size, A, B):
    for i in range(size):
        for j in range(i+1, size):
            if(abs(A[i][i]) < abs(A[j][i])):
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
                aux1 = B[i]
                B[i] = B[j]
                B[j] = aux1
# Faz a leitura de baixo pra cima da matriz, resolvendo o sistema e 
# retornando o vetor resultante.   
def lu (size, A, B):
    global I
# Preenchendo a matriz I com a diagonal principal substituida por 1.
    for i in range(size):
        linha_I = [0.0]*size
        for j in range(size):
            if(i == j): linha_I[j] = 1.0
        I.append(linha_I)

    pivo(size, A, B)
    # Zerando os valores abaixo da diagonal principal e 
    # montando a matriz U. Montando a matriz L com os 
    # valores preenchidos na diagonal principal e acima dela.
    aU = matriz_LU(size, A)
    # Pegando a matriz I
    aL = I
    
    y = [0.0]*size
    x = [0.0]*size
    y[0] = B[0] / aL[0][0]
    
    for i in range(1, size):
        s = 0.0
        for j in range(size):
            s = s + (aL[i][j] * y[j])
        y[i] = (B[i] - s) / aL[i][i]

    x[size-1] = y[size-1] / aU[size-1][size-1]
    for i in range(size-1, -1, -1):
        s = 0.0
        for j in range(i+1, size):
            s = s + (aU[i][j] * x[j])
        x[i] = (y[i] - s) / aU[i][i] 

    return x