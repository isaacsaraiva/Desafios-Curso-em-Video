altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

print('A largura da parede é igual a {}m e a altura é {}m, logo, a área é {}m²\n'
      'Para esta parede, precisará de {:.2f} litros de tinta.'
      .format(altura, largura, altura * largura, (altura * largura) / 2))
