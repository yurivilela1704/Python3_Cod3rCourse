limite = float(input('Digite o valor que deseja ser o limite: '))

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # .append é para adiciocar um dado a lista
        # resultado[-2] é para escolher um intem da lista(nesse caso começando do final)
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(limite):
        print(fib)
