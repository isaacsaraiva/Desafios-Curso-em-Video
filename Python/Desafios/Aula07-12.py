preco = float(input('Digite o preço do produto: R$'))

print('O produto tinha como seu preço R${:.2f} mas com o desconto de 5%, passou a ser apenas R${:.2f}'
      .format(preco, (preco / 100) * 95))
