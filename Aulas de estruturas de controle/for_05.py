# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#    print('Fim')

# CRIAR UM ALGORITMO QUE:
# gere um dado entre 1 e 6 aleatoriamente
# se for impar continue
# se o numero for par e for igual o valor sorteado
# imprimir 'acertou' e dar break
# se nao acertar ir para o else.... ''ERROOOOOU'

from random import randint

def sortearDados():
    return randint(1, 6)


for numero in range(1, 7):
    if numero % 2 == 1:
        continue

    if sortearDados() == numero:
        print('Acertou', numero)
        break
else:
    print('Erouuuuu', numero)
