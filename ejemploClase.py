#-*- coding: utf-8 -*-

class Humano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

jairo = Humano('Jairo', 29)
zahira = Humano('Zahira', 30)

print('Hola soy {}, y tengo {} años'.format(jairo.nombre, jairo.edad))
print('Hola soy {}, y tengo {} años'.format(zahira.nombre, zahira.edad))


