# -*- coding: utf-8 -*-

def foreing_exchange_calculator(ammount):
    aus_to_col_rate = 2319

    return aus_to_col_rate * ammount


def run():
    print('CALCULADORA DE DIVISAS')
    print('Convertir Dollar Australiano a pesos colombianos')
    print('')

    ammount = float(input('Ingresa la cantidad de Dolares que quieres convertir: '))

    result = foreing_exchange_calculator(ammount)

    print('${} dolares Australianos son ${} pesos colombianos'.format(ammount,result))
    print('')

if __name__ == '__main__':
    run()