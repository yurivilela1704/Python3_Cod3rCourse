# O generator ele gera a lista sob demanda, isso faz com que ele consuma muito menos memoria

generator = (i ** 2 for i in range(10) if i % 2 == 0 )

for numero in generator:
    print(numero)
