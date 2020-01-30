#-*- coding: utf-8 -*-

def run():
    while True:
        command = str(input('''Bienvenido
        
        Qué deseas hacer??
        
        [a]ñadir vehículo
        [b]uscar vehículo por placa
        [s]alir
        
        '''))

        if command == 'a':
            print('vehículo añadido')
        elif command == 'b':
            print('ingrese la placa que desea buscar: ')
        else:
            print('Vuelva pronto!! ')





if __name__ == '__main__':
    run()