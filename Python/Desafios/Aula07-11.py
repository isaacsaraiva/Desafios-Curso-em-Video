altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

print('A largura da parede é igual a {} e a altura é {}, para este valor, precisará de {} latas de tinta.'
      .format(altura, largura, (altura * largura) / 2 ))