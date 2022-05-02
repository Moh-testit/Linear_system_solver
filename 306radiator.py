#!/usr/bin/python3

import math
import sys


def usage(args):
    if '-h' in args:
        print('USAGE')
        print('\t' + sys.argv[0] + ' n ir jr [i j]\n')
        print('DESCRIPTION\n\tn\t\tsize of the room')
        print('\t(ir, jr)\tcoordinates of the radiator\n\t(i, j)\t\tcoordinates of a point in the room')
        sys.exit(0)

def chk_err(*args, **indvalue):
    file = indvalue.pop('file', sys.argv[0])
    print(file + ':', *args, **indvalue, file=sys.stderr)
    sys.exit(84)


def functionnal_check(n, value=0):
    n *= 10**value
    n = math.floor(n) if n - math.floor(n) < 0.5 else math.ceil(n)
    return n / 10**value


def coordonate(args):
    try:
        lst, ir, jr = (int(x) for x in args[:3])
        if lst < 3 or not all(1 <= x <= (lst - 2) for x in (ir, jr)):
            raise ValueError
        n = lst**2
        r = ir + jr * lst
    except ValueError:
        chk_err('invalid argument')
    def term(i, j):
        if not all(1 <= x <= (lst - 2) for x in (i % lst, i // lst)):
            return 1.0 if i == j else 0.0
        else:
            a = abs(i - j)
            if a == 0:
                return -16.0
            if a == 1 or a == lst:
                return 4.0
            return 0.0
    A = [[term(i, j) for j in range(n)] for i in range(n)]
    N = list(range(n))
    if len(args) == 3:
        for a in A:
            print('\t'.join('%d' % r for r in a))
        print()
    for i in range(n):
        A[i].append(-300 if i == r else 0)

    for k in range(n):
        for i in range(k, n):
            if abs(A[i][k]) > abs(A[k][k]):
                A[k], A[i] = A[i], A[k]
                N[k], N[i] = N[i], N[k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] -= f * A[k][j]

    T = [0.0] * n
    T[n - 1] = A[n - 1][n] / A[n - 1][n - 1]
    for i in reversed(range(n)):
        c = 0.0
        for j in range(i + 1, n):
            c += A[i][j] * T[j]
        T[i] = (A[i][n] - c) / A[i][i]

    if len(args) == 3:
        for t in T:
            print('%.1f' % functionnal_check(t, 1))
    else:
        try:
            i, j = (int(x) for x in args[3:5])
            if not all(0 <= x <= (lst - 1) for x in (i, j)):
                raise ValueError
        except ValueError:
            chk_err('invalid argument')
        print('%.1f' % functionnal_check(T[i + j * lst], 1))


def main(args):
    usage(args)
    if len(args) not in (3, 5):
       chk_err('invalid number of arguments')
    
    coordonate(args)


if __name__ == '__main__':
        main(sys.argv[1:])
