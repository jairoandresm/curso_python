#-*- coding: utf-8 -*-

def averrage(temps):

    sum_of_temps = 0

    for t in temps:
        sum_of_temps += float(t)
    return sum_of_temps / len(temps)


if __name__ == '__main__':
    temps = [22,21,25,24,24,20,19]

    result = averrage(temps)
    print('El promedio de temperatura es: {}'.format(result))

