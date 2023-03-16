from math import sin, cos, tan, radians

num = float(input('Digite o valor do ângulo: '))

print('O número {}, tem como seu seno igual a {:.3f}, o cosseno igual a {:.3f} e a tangente igual {:.3f}.'
      .format(num, sin(radians(num)), cos(radians(num)), tan(radians(num))))
