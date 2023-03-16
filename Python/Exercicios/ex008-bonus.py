metros = float(input('Digite a quantidade de metros que deseja converter: '))

print('A quatidade de {} metros convertida em:\n'
      'Kilometros é igual a: {}km\n'
      'Hectometros é igual a: {}hm\n'
      'Decametros é igual a: {}dam\n'
      'Decimetros é igual a: {}dm\n'
      'Centimetros é igual a: {}cm\n'
      'Milimetros é igual a: {}mm\n'
      .format(metros, metros / 1000, metros / 100, metros / 10, metros * 10, metros * 100, metros * 1000))
