def getTipoDia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, 'Inválido')


for dia in range(8):
    print(f'{dia}: {getTipoDia(dia)}')
