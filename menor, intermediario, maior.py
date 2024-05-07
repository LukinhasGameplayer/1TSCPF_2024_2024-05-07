n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))


print(f'Os números: {n1}, {n2}, {n3}', end = '' )
if n1 > n2:
    n1, n2 = n2, n1

if n1 > n3:
    n1, n3 = n3, n1

if n2 > n3:
    n2, n3 = n3, n2

print(f'São menor: {n1}, inter: {n2} e maior: {n3}')
