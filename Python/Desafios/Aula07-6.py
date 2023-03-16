num = float(input('Digite o número que queira saber o dobro, triplo e a raiz quadrada: '))

print("O número que digitastes foi o '{}', o dobro dele é '{:.2f}', o triplo é '{:.2f}' e a raiz quadrada é '{:.2f}'."
      .format(num, num * 2, num * 3, num ** (1/2)))
