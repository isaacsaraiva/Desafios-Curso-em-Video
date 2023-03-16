oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))

print('Considerando o valor do cateto oposto igual a {} e o adjacente igual a {},'
      ' o valor da hipotenusa é igual a {:.2f}'
      .format(oposto, adjacente, (oposto ** 2 + adjacente ** 2) ** (1 / 2)))


#usando o modulo math:
#
#from math import hypot
#
#oposto = float(input('Qual o valor do cateto oposto? '))
#adjacente = float(input('Qual o valor do cateto adjacente? '))
#hipotenusa = math.hypot(oposto, adjacente)
#
#print('Considerando o valor do cateto oposto igual a {} e o adjacente igual a {},
# o valor da hipotenusa é igual a {:.2f}'
#     .format(oposto, adjacente, hipotenusa))
#
#
