frase = input('Digite uma frase: ')

print("A letra 'A' aparece: {} vezes.\n"
      "A posição que ela aparece a primeira vez é na {}.\n"
      "A posição que ela aparece a última vez é na {}."
      .format(frase.count('A'), frase.find('A'), frase.rfind('A')))
