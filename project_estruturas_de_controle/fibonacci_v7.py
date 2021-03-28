quantidade = int(input('Digite a quantidade de sequencia de fibo que deseja: '))


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib)