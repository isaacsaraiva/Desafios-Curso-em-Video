real = float(input('Digite qual o valor pretende converter para dólar: '))

print('O valor R${} convertido para dólar fica igual a ${:.2f}. (Cotação atual: 3.27).'
      .format(real, real / 3.27))
