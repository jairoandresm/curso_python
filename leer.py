# -*- coding: utf-8 -*-

import json

def run():
# se crea una contador para saber cuantas veces aparece una palabra
    counter = 0
    with open('DATA.json') as f:
        #rint(f.readlines()) lee las líneas creando una lista de cada documento
        for line in f:
            counter += line.count('LA202')
    print('La norma aparece {} veces en el documento'.format(counter))


if __name__ == '__main__':
    run()