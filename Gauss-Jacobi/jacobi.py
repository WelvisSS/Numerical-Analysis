# Este método calcula a norma entre os vetores v e x.
def norma(V, X):
    # Variáveis auxiliares
    numAnterior, denAnterior = 0, 0
    # Laço que procura os maiores numeradores e denominadores.
    for i in range(len(V)):
        # Calculando o numerador atual.
        num = abs(V[i] - X[i])
        # Calculando o denominador através do módulo 
        # da aproximação atual.
        den = abs(V[i])
        # Veridica se o numerador é maior que o maior
        # numerador já encontrado.
        if num > numAnterior: numAnterior = num
        # Verifica se o denominador é maior que o 
        # maior denominador já encontrado.
        if den > denAnterior: denAnterior = den
    # Retorna a divisão do maior numerador pelo maior 
    # denominador.
    return numAnterior/denAnterior
# Método principal.
# Transformando o sistema Ax=b em x=Cx+g, transformando a 
# matriz A diretamente na matriz C e o vetor b no vetor g.
def jacobi(n, A, B, epsilon, iter):
    # Craindo os vetores x e v com base no tamanho de A.
    x = [0 for i in range(n)]
    v = [0 for i in range(n)]
    # Laços responsáveis por calcular o valor de cada posição da 
    # matriz A e vetor b, percorrendo linhas 'i' e colunas 'j'.
    for i in range(n):
        for j in range(n):
            # Quando o elemento não pertencer a diagonal principal
            # Atribui a uma posição ij que não seja igual a 
            # diagonal principal, o valor da sua divisão pelo 
            # elemento da diagonal principal da linha do valor.
            if i != j: A[i][j] /= A[i][i]
        # b[i] vai receber o seu valor dividido pelo elemento da 
        # diagonal principal que está na mesma linha que ele.
        B[i] /= A[i][i]
        # Recebe todos os resultados obtidos em b.
        x[i] = B[i]
    # Laço que determina o número de iterações feitas.
    for k in range(1, iter+1):
        # Laço que percorre as linhas.
        for i in range(n):
            # Variável que armazena o somatório.
            somatorio = 0
            # Laço que percorre as colunas.
            for j in range(n):
                # Verificação se o elemento não pertence a diagonal principal.
                # Fazendo o somatório das linhas e produto pelo resultado 
                # em x que é a aproximação anterior, e armazenando em S.
                if i != j: somatorio += A[i][j] * x[j]
            # Calculando a diferença entre b e o resultado do somatório 
            # para a linha em questão.
            v[i] = B[i] - somatorio
        # Fazendo o cálculo da norma entre v que é o resultado do 
        # somatório e x que é o resultado obtido através da divisão 
        # de b e a diagonal principal.
        result = norma(v, x)
        # se a norma for menor ou igual a precisão, termina o processo retornando v.
        if result <= epsilon: return v
        # Caso contrário, x recebe v e o processo é feito novamente 
        # até que a precisão seja atingida ou o número de iterações seja alcançado.
        x = [i for i in v]

#Leitura do arquivo de entrada.
file_in = open('input.txt', 'r')
#Leitura do arquivo de saída.
file_out = open('output.txt', 'w')
A = []
B = []
# Pegando o valor acima da matriz que representa o número de linhas.
size = int(file_in.readline())
# Pegando o valor acima da matriz que representa a precisão.
epsilon = float(file_in.readline())
# Laço que faz a leitura de cada linha montando a matriz linha por linha.
for i in range(size):
    linha = []
    # Faz a leitura da linha em questão
    valores_linha = file_in.readline()
    # Remove o '\n'
    valores_linha = (valores_linha.replace('\n', ''))
    # Divide os elementos com base no espeço entre eles.
    valores_linha = valores_linha.split(' ')
    # Faz a varredura do vetor A e armazena em 'linha'.
    for j in range(len(valores_linha)-1):
        linha.append(float(valores_linha[j]))
    # Armazena o valor da última coluna referente ao vetor B
    B.append(float(valores_linha[j+1]))
    #Armazena da coluna 0 a coluna n-1, referentes ao vetor A
    A.append(linha)
# Resolvendo o sistema.
file_out.write(str(jacobi(len(A), A, B, epsilon, 50)) + '\n')
# Fechando os arquivos.
file_in.close()
file_out.close()