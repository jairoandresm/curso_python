#-*- coding: utf-8 -*-
class Lama:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
#Se crea una lista vacía para guardar los datos

class Datos:
    def __init__(self):
        self.datos = []

    def add(self, nombre, apellido, email):
        dato = Lama(nombre, apellido, email)
        self.dato.append(datos)


def _print_contact(self, datos):
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')
        print('Nombre: {}'.format(dato.nombre))
        print('Teléfono: {}'.format(dato.apellido))
        print('Email: {}'.format(dato.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')



def run():
    while True:
        command = str(input('''Bienvenido
        
        Qué deseas hacer??
        
        [r]egistrar Usuario
        [b]uscar usuario
        [s]alir
        
        '''))

        if command == 'r':
            nombre =  str(input('Escribe el nombre del contacto: '))
            apellido =  str(input('Escribe el apellido del contacto: '))
            email =  str(input('Escribe el email del contacto: '))
            
            dato.add(nombre, apellido, email)

        elif command == 'b':
            print('ingrese el nombre de la persona que desea buscar: ')
        elif command == 's':
            print('Vuelva pronto!! ')
        else:
            print('Comando no encontrado ')
            





if __name__ == '__main__':
    run()