cidade = input('Digite o nome da cidade: ')
primeiro = cidade.upper().split()

print('O nome da sua cidade começa com {}, sendo o requisito {}.'
      .format(primeiro[0], 'SANTO' in primeiro))
