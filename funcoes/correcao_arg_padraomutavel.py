def fibonacci(sequencia=[0, 1]):
    # Uso de mutaveis como valor default (its a trap)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


inicio = fibonacci()
print(inicio, id(inicio))
print(fibonacci(inicio))
restart = fibonacci()
print(restart, id(restart))
