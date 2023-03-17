nome = input('Digite seu nome completo: ')
primeiro = nome.split()

print('O nome todo maiúsculo fica: ', nome.upper())
print('O nome todo minúsculo fica: ', nome.lower())
print('O nome sem espaços tem ao todo:', len(nome.replace(' ', '')), 'letras')
print('O primeiro nome tem: ', len(primeiro[0]), 'letras')
