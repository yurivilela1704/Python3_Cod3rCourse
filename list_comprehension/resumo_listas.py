# RESUMÃO SOBRE LISTAS

dobrosNormal = [0, 2, 4, 6]
# .append feito para adicionar valores a lista
dobrosNormal.append(8)
print(dobrosNormal)
# len > feito para ver quantidade de dados na lista
print(len(dobrosNormal))
# feito para remover um dado da lista(não é removido o dado do indice 0 e sim o proprio 0 na lista)
dobrosNormal.remove(0)
print(dobrosNormal)
# reverte e altera a lista
dobrosNormal.reverse()
print(dobrosNormal)
# index > ao passar o valor da lista ele te devolve o indice(sempre comecando do zero)
print(dobrosNormal.index(6))
# [-1] comeca a pegar os itens na lista de trás para frente, sendo -1 o primeiro
print(dobrosNormal[-1])
# ACESSANDO LISTAS
# percore e resgata o primeiro da lista e o ultimo(sendo que, o ultimo é uma antes do indice passado)
print(dobrosNormal[1:3])
# do indice indicado um até um antes do ultimo da lista
print(dobrosNormal[1:-1])
# do indice indicado ate o ultimo da lista
print(dobrosNormal[1:])
# do começo da lista até o indice indicated
print(dobrosNormal[:-1])
# mesmo que acessar apenas a lista
print(dobrosNormal[:])
# o primeiro seria daria o inicio, o segundo o fim e o terceiro indica os saltos
# (no caso abaixo. percorre toda lista 2 em 2)
print(dobrosNormal[::2])
# deletando item por indice
del dobrosNormal[3]
print(dobrosNormal)
