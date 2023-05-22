from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adijacente'))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}' .format(h1, hypot(co,ca)))



