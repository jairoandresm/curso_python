class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        suma_total = self.num1 + self.num2
        return suma_total

    def resta(self):
        resta_total = self.num1 - self.num2
        return resta_total
    
    def producto(self):
        producto = self.num1 * self.num2
        return producto

    def divisor(self):
        dividido = self.num1 / self.num2
        return dividido


print('-*-*-*-*-*-*-*-*-*-*-*-')
a = int(input('Ingrese el primer valor: '))
b = int(input('Ingrese el segundo valor: '))
print('-*-*-*-*-*-*-*-*-*-*-*-')


calc = Calculadora(a,b)

print('La suma de los valores es: ', calc.suma())
print('La resta de los valores es: ', calc.resta())
print('La multiplicación de los valores es: ', calc.producto())
print('La división de los valores es: ', calc.divisor()) 