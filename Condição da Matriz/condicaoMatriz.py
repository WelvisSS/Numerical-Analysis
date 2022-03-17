# Calcula a inversa de Gauss Jordan
def inverseGausJordan(n, mat2):
    # Matriz que terá o resultado
    inv = []
    # Matriz auxiliar que terá a
    # matriz original e o resultado.
    mat = []
    # Criando a matriz resultado
    for i in range(n):
        inv.append([])
        for j in range(n):
            inv[i].append(0)
    #Criando a matriz auxiliar
    for i in range(2*n):
        mat.append([])
        for j in range(2*n):
            mat[i].append(0)
    # Colocando os valores da matriz original na auxiliar.
    for i in range(n):
        for j in range(n):
            mat[i][j] = mat2[i][j]
    # Inicializando lado direito da matriz de identidade
    for i in range(n):
        for j in range(2*n):          
            if j == i+n: mat[i][j] = 1    
    # Pivotamento parcial
    i = n
    while(i > 1):
        i -= 1
        if mat[i-1][1] < mat[i][1]:        
            for j in range(2*n):
                d = mat[i][j]
                mat[i][j] = mat[i-1][j]
                mat[i-1][j] = d    
    # Reduzindo para Matriz Diagonal
    for i in range(n):
        for j in range(2*n):
            if j != i: 
                d = mat[j][i] / mat[i][i]
                for k in range(2*n): mat[j][k] -= mat[i][k]*d    
    # Reduzindo para a matriz de unidade
    for i in range(n):
        d = mat[i][i]
        for j in range(2*n): mat[i][j] = mat[i][j]/d

    # Insere o inverso da matriz de entrada em inv
    for i in range(n):
        for j in range(n, 2*n):
            # inv[i][j-n] = round(mat[i][j], 2)
            inv[i][j-n] = mat[i][j]
    # Retornando a matriz inversa.
    return inv
# Calcula a norma da matriz passada.
def norma(matriz):
    maxNum = 0
    norm = []
    # Pega os maiores valores em módulo de cada linha da matriz.
    for i in range(len(matriz)):
        maxNum = 0
        for j in range(len(matriz)):
            if maxNum < abs(matriz[i][j]): maxNum = abs(matriz[i][j])
        norm.append(maxNum)
    # Faz o somatório dos maiores valores obtidos de cada linha da matriz.
    return sum(norm)
# Calcula a condição da matriz
def condicaoMatriz(matriz):
    # Calcula a norma da matriz inicial.
    normaMatriz = norma(matriz)
    # Calcula a inversa da matriz inicial.
    inversaMatriz = inverseGausJordan(len(matriz), matriz)
    # Calcula a norma da inversa da matriz inicial.
    normaInversa = norma(inversaMatriz)
    # Produto da norma da matriz com norma da inversa da matriz.
    condicao = normaMatriz*normaInversa
    # Retorna o resultado.
    return condicao

#Leitura do arquivo de entrada.
entrada = open('input.txt', 'r')
#Leitura do arquivo de saída.
saida = open('output.txt', 'w')
# Criando os vetores A e B vazios.
A = []
# Pegando o valor acima da matriz que representa o número de linhas.
size = int(entrada.readline())
# Criando uma lista com o tamanho especificado
#Laço que faz a leitura de cada linha montando a matriz linha por linha.
for i in range(size):
    linha = []
    #Faz a leitura da linha em questão
    valores_linha = entrada.readline()
    #Remove o '\n'
    valores_linha = (valores_linha.replace('\n', ''))
    #Divide os elementos com base no espeço entre eles.
    valores_linha = valores_linha.split(' ')
    # Faz a varredura do vetor A e armazena em 'linha'.
    for j in range(len(valores_linha)):
        linha.append(float(valores_linha[j]))   
    #Armazena da coluna 0 a coluna n-1, referentes ao vetor A
    A.append(linha)
# Executando o método principal e gravando o resultado ao mesmo tempo.    
saida.write(str(condicaoMatriz(A)) + '\n')
# Fechando os arquivos.
entrada.close()
saida.close()