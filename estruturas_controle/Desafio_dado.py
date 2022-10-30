# criar uma função, um dado de 6 lados (1, 7)
# for com range, excluir o impar (continue), se for par
#  e == ao valor sorteado pela função dado (print 'acertou mizeravi') break
# se nao acertar chma o break


from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == 1:
        print('Acertou mizeravi!!',  i)
        break
else:
    print('Nao foi dessa vez!')
