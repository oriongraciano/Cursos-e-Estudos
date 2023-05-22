# import math
#num = float(input('Digite um número para-se obter a raiz quadrada: '))
#raiz = math.sqrt(num) #Nessa linha e necessario carregar a função que quer da biblioteca
#print('A raiz quadrada de {} e igual a {}' .format(num, raiz))


# o metodo a abaixo ira trazer somente a função selecionanda da biblioteca selecionada:
# Exp:
from math import sqrt
num = float(input('Digite um número para-se obter a raiz quadrada: '))
raiz = sqrt(num) #nessa linha não foi necessario carregar a funcão da biblioteca, pois a mesma ja foi passada acima.
print('A raiz quadrada de {} e igual a {}' .format(num, raiz))








