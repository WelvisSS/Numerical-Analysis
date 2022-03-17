I = []

def matriz_LU (size, A):
    for k in range(size):
        for i in range(k+1, size):
            m = A[i][k] / A[k][k]
            A[i][k] = 0.0
            I[i][k] = m
            for j in range(k+1, size):
                A[i][j] = A[i][j] - (m * A[k][j])
    
    return A
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
def lu (size, A, B):
    global I
    for i in range(size):
        linha_I = [0.0]*size
        for j in range(size):
            if(i == j): linha_I[j] = 1.0
        I.append(linha_I)

    pivo(size, A, B)
    aU = matriz_LU(size, A)
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