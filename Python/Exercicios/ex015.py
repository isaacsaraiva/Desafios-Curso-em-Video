dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Qual a kilometragem percorrida durante esse tempo? '))

print('Com o carro sendo alugado por {}dias e tendo percorrido {}km, o valor do aluguel ficará em R${:.2f}.'
      .format(dias, km, (dias * 60) + (km * 0.15)))
