#-*- coding: utf-8 -*-

class Contact:

    #constructor que recibe los contactos del usuario
    def __init__(self, name, phone, email): 
        self.name = name 
        self.phone = phone
        self.email = email

#esta lista vacía va a guardar los contactos
class ContactBook:
    def __init__(self):
        self._contacts = []  

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break
    
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break

        else:
            self._not_found()
           


    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')

    def _not_found(self):
        print('***********')
        print('¡No encontrado!')
        print('***********')

def run():

    contact_book = ContactBook()
    while True:
        command = str(input('''
            Qué deseas hacer?
          
            [a]ñadir cintacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
            '''))
        
        if command == 'a':
            name =  str(input('Escribe el nombre del contacto: '))
            phone =  str(input('Escribe el teléfono del contacto: '))
            email =  str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)


        elif command == 'ac':

            name =  str(input('Escribe el nombre del contacto a actualizar: '))


            

        elif command == 'b':
            
            name =  str(input('Escribe el nombre del contacto que busca: '))
            contact_book.search(name)

        
            contact_book.delete(name)
        elif command == 'l':
            
            contact_book.show_all()

        elif command == 's':
            print('adios')
            break
        else:
            print('Comando no encontrado')







if __name__ == '__main__':
    run()