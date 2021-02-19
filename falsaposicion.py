import numpy as np 

funcion = lambda x: x**4 + 2* (x**2) - x - 3


a = 0
b = 2
tolerancia = 0.0001
tramo = abs(b-a)
#procedimiento


while not (tramo<= tolerancia):
    fa = funcion(a)
    fb = funcion(b)
    c = b - fb * (a-b) / (fa-fb)
    fc = funcion(c)

    cambio = np.sign(fa)*np.sign(fc)

    if cambio > 0:
        tramo = abs(c-a)
        a = c
    else:
        tramo = abs(b-c)
        b = c

print(c)
print (tramo)
print ("primera modificacion")