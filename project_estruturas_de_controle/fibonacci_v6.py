quantidade = float(input('Digite a quantidade de sequencia de fibo que deseja: '))


def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
        elif quantidade < 0:
            print('A quantidade precisa ser maior que 0')
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib)
