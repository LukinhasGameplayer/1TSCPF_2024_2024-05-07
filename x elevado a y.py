# base = float(input('Digite o valor da base(que seja maior que 1): '))
# exponencial = float(input('Digite o valor do exponencial(que seja maior ou igual a 2): '))
#
# calculo = base ** exponencial
# # if base < 1 or exponencial < 2:
#     print('Valor invalido')
#
# elif base > 1:
#     if exponencial >= 2:
#         print(calculo)
base = int(input('Digite o valor da base(que seja maior que 1): '))
exponencial = int(input('Digite o valor do exponencial(que seja maior ou igual a 2): '))

total = 1
i = 1
if base <= 1 or exponencial < 2:
    print('ERRO')
else:
    # for _ in range(exponencial):
    #     total = total * base
    # print(f'{base} elevado {exponencial} é igual à {total}')
    while i <= exponencial:
        #total = total * base
        total += base
        i += 1
        print(f'{base} elevado {exponencial} é igual à {total}')
