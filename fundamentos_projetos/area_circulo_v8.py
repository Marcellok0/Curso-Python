#!/usr/local/bin/python3

from cmath import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
