# palavra1 = ' REVIVER'
# palavra2 = ' '
#
# frase = palavra1 + '' + palavra2
# print(frase)
#
# fraseinversa = palavra2 + '' + palavra1
# print(fraseinversa)

palavra = input('Digite a palavra: ')
reversa = ''
resp = 's'
while resp in('s', 'sim', 'y', 'yes', 'si'):
  palavra = input('Digite a palavra: ')
  reversa = ''
  for letra in palavra:
     reversa = letra + reversa
  if palavra == reversa:
     print(f'A palavra {palavra} é polidromo')
  else:
     print(f'A palavra {palavra} não é polidromo')

  resp = input('Quer continuar a brincar?').lower()
