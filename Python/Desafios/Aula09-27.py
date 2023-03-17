nome = input('Digite o nome completo: ')
primeiro = nome.split()

print('O seu nome {} contém:'
      'O primeiro nome é: {}\n'
      'O último nome é: {}'
      .format(nome, primeiro[0], primeiro[-1]))
