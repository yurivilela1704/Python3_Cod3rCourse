palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end='')


aprovados = ['Rafaela', 'Pedro', 'Yuri', 'Andréia', 'Néria']


for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)
