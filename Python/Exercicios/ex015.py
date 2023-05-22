print('--EXERCICIO 15--')
dias = int(input('Quantos dias foi alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))


