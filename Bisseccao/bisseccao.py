from math import *
from numpy import *

# Recebe a função e o valor de substituição em x.
def function(funcao, x):
	return eval(funcao)

def bissection (f, a, b, epsilon):	
	# Se o produto de f(a) com f(b) resultar em um núemro
	# menor que 0, significa que exeiste uma raiz no intervalo [a, b], 
	# logo, podemos calcular para estes valores.	
	if(function(f, a) * function(f, b) < 0):
		iteracoes = 1
		# Ponto médio
		x = (a+b)/2
		# Condição de parada, quando o resultado da função for menor que a precisão.
		while(abs(b-a) > epsilon):
			# Condição de troca de valor dos extremos.
			if (function(f, a) * function(f, x) < 0) :
				b = x				
			else:
				a = x
			# Ponto médio
			x = (a+b)/2
			# Contando as iterações.
			iteracoes = iteracoes + 1
		# Gravando os resultados no arquivo de saida
		file_output.write("f(x) = {}" .format(str(f)))
		file_output.write("Iterações = {}\n" .format(str((iteracoes))))
		file_output.write("εa = {}\n" .format(str((b - a))))
		file_output.write("c = {}\n" .format(x))
		file_output.write("f(c) = {}\n\n\n" .format(function(f, x)))

	else: print('Não existe raiz neste intervalo')
		
# Abrindo os arquivos.
file_input = open('input.txt', 'r');
file_output = open('output.txt','w')
while(True):
	# Lendo a função.
	func = file_input.readline()
	# Lendo o extremo a.
	a = (float)(file_input.readline())
	# Lendo o extremo b.
	b = (float)(file_input.readline())
	# Lendo a precisão.
	epsilon = (float)(file_input.readline())
	# Executando o método.
	bissection(func, a, b, epsilon)
	if(file_input.readline() == ""): break
	# Fechando os arquivos.
file_input.close()
file_output.close()