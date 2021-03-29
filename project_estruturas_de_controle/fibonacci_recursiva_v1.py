quantidade = float(input('Digite a quantidade de sequencia de fibo que deseja: '))


def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]), ))


if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib)
