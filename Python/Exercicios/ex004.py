text = input('Digite algo que queira obter todas as informações possiveis: ')
print('O que colocastes é do tipo:', type(text))
print('Contém apenas espaços?', text.isspace())
print('É apenas formado por números?', text.isnumeric())
print('É apenas formado pelas letras alfabéticas?', text.isalpha())
print('É formado por números e/ou letras?', text.isalnum())
print('É escrito apenas em maiúsculas?', text.isupper())
print('É escrito apenass em minúsculas?', text.islower())
print('Está capitalizada?', text.istitle())
