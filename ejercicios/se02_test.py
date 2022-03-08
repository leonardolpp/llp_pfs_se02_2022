# Auth: Leonardo Perez
# Version: 0.2.1
# date: 02/03/2022
# dupdateAt: --/--/----
'''
# Python: Formateo de cadenas
# %c = str, simple carácter.
# %s = str, cadena de carácter.
# %d = int, enteros.
# %f = float, coma flotante.
# %o = octal.
# %x = hexadecimal.
'''
K = 1.0234

pi = math.pi
M = 10.01
# L = math.fsum(K)

tipo = 'Suma'

print('La %s de %.3f y %.3f por pi es: %.6f' % (tipo, K, L, M))
print('Valor de pi: %.16f' % pi)
