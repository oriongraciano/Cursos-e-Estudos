from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja'))
seno = sin(radians(angulo))
print('O anglo de {} SENO de {:.2f}' .format(angulo, seno))
cosseno = cos(radians(angulo))
print('O anglo de {} COSENO de {:.2f}' .format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O anglo de {} SENO de {:.2f}' .format(angulo, tangente))


