# O generator ele gera a lista sob demanda, isso faz com que ele consuma muito menos memoria

generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator)) # saida 0
print(next(generator)) # saida 4
print(next(generator)) # saida 16
print(next(generator)) # saida 36
print(next(generator)) # saida 64
print(next(generator)) # ERRO
