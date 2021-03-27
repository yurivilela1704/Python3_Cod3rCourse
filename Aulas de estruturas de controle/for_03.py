produto = {'nome': 'Caneta bic', 'preco': 10.99,
           'importada': True, 'estoque': 793}


for chaves in produto:
    print(chaves)


for valor in produto.values():
    print(valor)


for chaves, valor in produto.items():
    print(f'{chaves} = {valor}')
