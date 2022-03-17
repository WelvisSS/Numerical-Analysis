def regressaoLinear (n, x, y):
    sumXY = 0.0
    sumXquadrado = 0.0
    
    for i in range(n):
        sumXY = sumXY + (x[i]*y[i])
        sumXquadrado = sumXquadrado + (x[i]**2)

    a = ((n * sumXY) - (sum(x) * sum(y))) / ((n * sumXquadrado) - (sum(x) ** 2))
    b = ((sum(y) * sumXquadrado) - (sum(x) * sumXY)) / ((n * sumXquadrado) - (sum(x) ** 2)) 
    
    file_output.write("a = {}\n" .format(a))
    file_output.write("b = {}\n" .format(b))
    file_output.write("Pontos = {}\n\n" .format(x))

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

while(1):
    x = file_input.readline().replace('\n', '').split(' ')
    y = file_input.readline().replace('\n', '').split(' ')

    x = [float(i) for i in x]
    y = [float(i) for i in y]

    regressaoLinear(len(x), x, y)
    if file_input.readline() == '': break


file_input.close()
file_output.close()