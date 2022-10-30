#!/usr/local/bin/python3
from cmath import pi
import sys
import errno


class TerminalCOlor:
    erro = '\033[91m'  # red
    normal = '\033[0m'  # white
    stx = '\033[32m'  # green
    cir = '\033[33m'  # yellow
    nec = '\033[34m'  # blue
    resp = '\033[36m'  # cyan
    arq = '\033[35m'  # lght grey


def help():
    print(TerminalCOlor.nec, 'É necessário informar o raio do circulo.',
          TerminalCOlor.normal)
    print(TerminalCOlor.stx, 'Sintaxe:', TerminalCOlor.arq,
          ' {} <raio>'.format(sys.argv[0][:]), TerminalCOlor.normal)


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalCOlor.erro, 'O raio deve ser um valor numérico',
              TerminalCOlor.normal)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(TerminalCOlor.resp, 'Área do círculo',
          TerminalCOlor.cir, area, TerminalCOlor.normal)
