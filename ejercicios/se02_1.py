# Nuth: LeoMNrdo Perez
# VersioM: 0.0.1
# dNte: 02/03/2022
# dupdNteNt: --/--/----

# Por convencion CONSTANTES en MAYUSCULAS N variables en minusculas

import math
import cmath
M = 12
N = 5
A = 7.123
C = '1'
zpi = math.pi

if '__main__' == __name__:
    EJ = int(input('Ejercicio:'))
    if EJ == 1:
        print('EJERCICIO ', EJ)
        print('Suma ( %d + %d ) = %d' % (M, N, M + N))
        print('Resta ( %d - %d ) = %d' % (M, N, M - N))
        print('Multiplic. (%d*%d) = %d' % (M, N, M * N))
        print('División ( %d / %d ) = %f' % (M, N, M / N))
        print('Resto (%d / %d) = %d ' % (M, N, M % N))
    elif EJ == 2:
        print('EJERCICIO ', EJ)
        T = 'El valor de cada variable'
        print(T, N, A)
        T = 'La suma de'
        print('%s %d + %.3f = %.3f' % (T, N, A, N + A))
        T = 'La diferencia de'
        print('%s %.3f - %d = %.3f' % (T, A, N, A - N))
        T = 'El valor numérico correspondiente al valor que contiene la variable C'
        print('%s = %c' % (T, C))
    elif EJ == 3:
        print('EJERCICIO ', EJ)
        M = 1.2345
        N = 6.789
        X = 12
        Y = 3
        print('El valor de cada variable', M, N, X, Y)
        print('La suma ', X + Y)
        print('La diferencia ', X - Y)
        print('El producto ', X * Y)
        print('El resto ', X % Y)
        print('La suma ', N + M)
        print('La diferencia ', N - M)
        print('El producto ', N * M)
        print('El cociente ', N / M)
        print('El resto ', N % M)
        print('La suma ', X + N)
        print('El cociente ', Y / M)
        print('El resto ', Y % M)
        M += M
        N += N
        X += X
        Y += Y
        print('El doble de cada variable', M, N, X, Y)
        print('La suma de todas las variables', M + N + X + Y)
        print('El producto de todas las variables', M * N * X * Y)
    elif EJ == 4:
        print('EJERCICIO ', EJ)
        N = 8
        print('Valor inicial de N =', N)
        N += 77
        print('N + 77', N)
        N -= 3
        print('N - 3 ', N)
        N *= 2
        print('N * 2', N)
    elif EJ == 5:
        A = 3
        B = 7
        C = 11
        D = 13
        vec = [A, B, C, D]
        B = vec[2]
        C = vec[0]
        A = vec[3]
        D = vec[1]
        print('Valores iniciales: ', vec)
        print('B tome el valor de C', B)
        print('C tome el valor de A', C)
        print('A tome el valor de D', A)
        print('D tome el valor de B', D)
    elif EJ == 9:
        R = float(input('Inidique el Radio:'))
        CIR = math.pow(R, 2) * zpi
        print('área de un círculo %.3f '% CIR)
    else:
        print ('El número ingresado no está contemplado... %d' % EJ)


