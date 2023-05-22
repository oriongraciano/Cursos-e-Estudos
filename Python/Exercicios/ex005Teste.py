print('---EXERCICIO 05---')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
dint = n1 // n2
expo = n1 ** n2
print('O resultado da soma é {}, O produto é {} e a divisão é {:.3f}' .format(soma, mult, div), end=' ')
print('O resultado da divisão inteira {} e á potência {}' .format(dint, expo))

