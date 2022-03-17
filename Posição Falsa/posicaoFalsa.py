# Importando bibliotecas necessárias.
from math import *
from numpy import *
# Recebe a função e o valor de substituição em x.
def function(funcao, x):
	# Retorna a conversão da string para uma função entendivel pelo código.
	return eval(funcao)
# Método principal.
def posicaoFalsa (f, a, b, epsilon):			
	# Se o produto de f(a) com f(b) resultar em um núemro
	# menor que 0, significa que exeiste uma raiz no intervalo [a, b], 
	# logo, podemos calcular para estes valores.
	if ((function(f, a) * function(f, b)) < 0):
		iteracoes = 1
		# Calculando raiz
		x = ((a * function(f, b)) - (b * function(f, a)))/(function(f, b) - function(f, a))		
		# Para quando o resultado da função é menor ou igual a precisão.
		while(abs(function(f, x)) > epsilon):			
			# Quando f(x) é menor que 0, a troca deve ser feita em b, 
			# substituindo pela nova raiz, caso contrário a troca é feita em a.
			if (function(f, a) * function(f, x) < 0) :
				b = x				
			else:
				a = x
			# Calculando nova raiz
			x = ((a * function(f, b)) - (b * function(f, a)))/(function(f, b) - function(f, a))
			# Contando as iterações
			iteracoes = iteracoes + 1
		# Gravando os resultados no arquivo de saída.
		file_output.write("f(x) = {}" .format(str(f)))
		file_output.write("Iteracao = {}\n" .format(str(iteracoes)))
		file_output.write("εa = {}\n" .format(str((b - a))))				
		file_output.write("c = {} \n" .format(str(x)))
		file_output.write("f(c) = {}\n\n\n" .format(str(function(f, x))))

	else: print('Não existe raiz neste intervalo')		
# Abrindo os arquivos.
file_input = open('input.txt', 'r');
file_output = open('output.txt','w')
while(True):
	# Leitura da  função.
	func = file_input.readline()
	# Leitura do extremo a.
	a = (float)(file_input.readline())
	# Leitura do extremo b.
	b = (float)(file_input.readline())
	# Leitura de epsilon.
	epsilon = (float)(file_input.readline())
	# Executando o método.
	posicaoFalsa(func, a, b, epsilon)
	if(file_input.readline() == ""): break
# Fechando os arquivos
file_input.close()
file_output.close()