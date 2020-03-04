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
        lama = Lama(nombre, apellido, email)
        self.datos.append(lama)

    def show_all(self):
        for dato in self.datos:
            self._print_contact(dato)

    def _print_contact(self, lama):
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')
        print('Nombre: {}'.format(lama.nombre))
        print('Teléfono: {}'.format(lama.apellido))
        print('Email: {}'.format(lama.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')



def run():

    mis_datos = Datos()
    while True:
        command = str(input('''Bienvenido
        
        Qué deseas hacer??
        
        [r]egistrar Usuario
        [l]istar contactos
        [s]alir
        
        '''))

        if command == 'r':
            nombre =  str(input('Escribe el nombre del contacto: '))
            apellido =  str(input('Escribe el apellido del contacto: '))
            email =  str(input('Escribe el email del contacto: '))

            mis_datos.add(nombre, apellido, email)

        elif command == 'l':
            mis_datos.show_all()
        elif command == 's':
            print('Vuelva pronto!! ')
        else:
            print('Comando no encontrado ')
            





if __name__ == '__main__':
    run()