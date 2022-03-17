# # Importando bibliotecas matemáticas necessárias.
from math import e, pi, tan, sin, cos
from sympy import diff, Symbol
# Método que faz a conversão da função em string para expressão entendível pelo código.
def function(funcao, x):
	return eval(funcao)
# Método principal, recebe os extremos a e b, a função, a 
# derivada da função, e o valor da precisão. 
def newton(a, b, f, devf, epsilon):
	# Condição que verifica se é possível calcular.
	
	if(function(f, a) * function(f, b) < 0):
		iteracao = 1
		# Ponto médio entre os intervalos.
		x1 = (a+b)/2		
		# Condição de parada, quando o resultado da função for menor que a precisão.
		while(abs(function(f, x1)) > epsilon):
			# Calculando a raiz
			x1 = x1 - (function(f, x1)/function(devf, x1))
			#Contando as iterações
			iteracao = iteracao + 1
		# Gravando o resultado.
		file_output.write("f(x) = {}" .format(str(f)))
		file_output.write("Iteracao = {}\n" .format(str(iteracao)))			
		file_output.write("c = {} \n" .format(str(x1)))
		file_output.write("f(c) = {}\n\n\n" .format(str(function(f, x1))))

	else: print('Intervalo sem raiz')
# Abrindo os arquivos.
file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')
while(1):
	# Lendo a função.
	func = file_input.readline()
	# Lendo o extremo a.
	a = float(file_input.readline())
	# Lendo o extremo b.
	b = float(file_input.readline())
	# Lendo a precisão.
	epsilon = float(file_input.readline())
	# Executando o método principal.
	x = Symbol('x')
	newton(a, b, func, str(diff(func)), epsilon)

	if(file_input.readline() == ""): break
# Fechando os arquivos
file_input.close()
file_output.close()