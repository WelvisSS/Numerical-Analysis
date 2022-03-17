# Deixando a matriz triangular zerando os números 
# abaixo da diagonal principal.
def mainDiagonal(size, A, B):
    # Chamando o método pivo.
    pivo(size, A, B)
    # Laço responsável pela triangulação.
    for k in range(size):
        if k == size-1: k = k - 1
        for i in range(k+1, size):
            # Definindo o multiplicador da linha
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, size):
                # Aqui fazemos a linha em questão menos o produto 
                # do multiplicador da linha pela linha do pivô.  
                A[i][j] = A[i][j] - (m * A[k][j])
            # Fazendo o mesmo processo que foi feito no vetor A só 
            # que no B.
            B[i] = B[i] - (m * B[k])            
# Verifica se para cada coluna o pivo é diferente de zero.
# Verifica também se o pivo é o maior número da sua coluna.
# Caso o pivô não seja o maior da sua coluna, é feita a 
# troca com o maior.
def pivo(size, A, B):
    for i in range(size):
        for j in range(i+1, size):
            if(abs(A[i][i]) < abs(A[j][i])):
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
                aux1 = B[i]
                B[i] = B[j]
                B[j] = aux1

#Resolve o sistema de baixo pra cima extraindo os resultados.
def gauss(size, A, B, X):
    # Efetua a eliminação chamando os métodos pivo e mainDiagonal,
    # e extrai os resultados obtidos.
    mainDiagonal(size, A, B)
    
    X[size-1] = B[size-1] / A[size-1][size-1]
    
    for i in range(size-1, -1, -1):
        s = 0.0
        for j in range(i+1, size):
            s = s + (A[i][j] * X[j])   
            # Extraindo os valores resultantes da matriz.         
            X[i] = (B[i] - s) / A[i][i] 
    # Vetor resultante.   
    return X

#Leitura do arquivo de entrada.
entrada = open('input.txt', 'r')
#Leitura do arquivo de saída.
saida = open('output.txt', 'w')
# Criando os vetores A e B vazios.
A = []
B = []
# Pegando o valor acima da matriz que representa o número de linhas.
size = int(entrada.readline())
# Criando uma lista com o tamanho especificado
X = [0.0]*size
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
    for j in range(len(valores_linha)-1):
        linha.append(float(valores_linha[j]))
    #Armazena o valor da última coluna referente ao vetor B
    B.append(float(valores_linha[j+1]))    
    #Armazena da coluna 0 a coluna n-1, referentes ao vetor A
    A.append(linha)
# Executando o método principal e gravando o resultado ao mesmo tempo.    
saida.write(str(gauss(size, A, B, X)) + '\n')
# Fechando os arquivos.
entrada.close()
saida.close()