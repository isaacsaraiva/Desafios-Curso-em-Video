nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print("A média das notas '{:.2f}' e '{:.2f}' é igual a '{:.2f}'"
      .format(nota1, nota2, (nota1 + nota2) / 2))
