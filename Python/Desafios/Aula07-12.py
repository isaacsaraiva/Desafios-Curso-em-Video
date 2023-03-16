preco = float(input('Digite o preço do produto: R$'))

print('O produto tinha como seu preço R${} mas com o desconto de 5%, passou a ser apenas R${}'
      .format(preco, (preco / 100) * 95))
