salario = float(input('Digite qual o valor do salário que será reajutado: R$'))

print('O salário de R${:.2f}, após sofrer um aumento de 15% passará a ser R${:.2f}.'
      .format(salario, (salario / 100) * 115))
