#-*- coding: utf-8 -*-

def palindrome(word):
    reverse_letter = word[::-1]
    print('La palabra {} al revés es: '.format(word))
    print(reverse_letter)

    if word == reverse_letter:
        print('La palabra {} es palìndromo'.format(word))
    else:
        print('La palabra {} NO es palìndromo'.format(word))


if __name__ == '__main__':

    word = str(input('Escribe tu palabra:  '))
    palindrome(word)

