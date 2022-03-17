# Importando biblioteca matemática necessária
from math import *
# Mátodo que faz a conversão da função em string para expressão entendível pelo código.
def function(funcao, x):
	return eval(funcao)
# método principal que resolve o sistema.
def secante(a, b, f, epsilon):
	# Condição que verifica se é possível calcular.
	if(function(f, a) * function(f, b) < 0):
		iteracao = 1		
		# Calculando a raiz.
		x = b - (function(f, b) * (b - a))/(function(f, b) - function(f, a))
		
		# Condição de parada, quando o resultado da função for menor que a precisão.
		while(abs(function(f, x)) > epsilon):
			# Trocando os valores para a próxima iteração.
			a = b
			b = x
			# Calculando a raiz.
			x = b - (function(f, b) * (b - a))/(function(f, b) - function(f, a))
			# Contador de iterações.
			iteracao = iteracao + 1
		# Gravando o resultado.
		file_output.write("f(x) = {}" .format(str(f)))
		file_output.write("Iteracao = {}\n" .format(str(iteracao)))			
		file_output.write("c = {} \n" .format(str(x)))
		file_output.write("f(c) = {}\n\n\n" .format(str(function(f, x))))
		
	else: print('Intervalo sem raiz')
# Abrindo os arquivos
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
	secante(a, b, func, epsilon)
	
	if(file_input.readline() == ""): break
# Fechando os arquivos.
file_input.close()
file_output.close()