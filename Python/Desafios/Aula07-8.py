metros = float(input('Digite o valor em metros que queira converter para centimetros(cm) e milimetros(mm): '))

print("O valor de '{}'metros é igual a {:.0f}cm e a {:.0f}mm."
      .format(metros, metros * 100, metros * 1000))
