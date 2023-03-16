preco = float(input('Qual o valor do produto? R$'))

print('O produto de preço R${} pode ser pago nas seguintes modalidades e valores respectivos:\n'
      'A vista: R${} - 10% de desconto.\n'
      'Parcelado: RS{} - 8% de juros.'
      .format(preco, (preco / 100) * 90, (preco / 100) * 108))
