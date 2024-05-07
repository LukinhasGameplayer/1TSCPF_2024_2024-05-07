frase = input('Digite sua frase: ')

vogais, consoantes, espacos = 0, 0, 0
for letra in frase:
    if letra in 'aeiouAEIOUáéíóúãêôõâ':
        vogais += 1
    elif letra == ' ':
        espacos += 1
    else:
        consoantes += 1

print(f'A frase:{frase} tem {vogais} vogais, {consoantes} consoantes, {espacos} espacos')
