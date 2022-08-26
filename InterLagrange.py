# Ana Sofía Escobar Rivera - 20489

#librerias necesarias para que funcione el programa 
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt #esta es para hacer graficos. 

# ingresamos los datos de nuestras matrices.
xi = np.array([1, 2, 3, 4, 5, 6, 7, 8]) #Cantidad de años analizados
#fi = np.array([19819643, 24411826, 32429311, 38076878, 43133089, 51273750, 65564512, 67917477]) #Venta mercancia
#fi = np.array([12087296, 14802522, 19872418, 22015823, 24031723, 28651153, 36878941, 37944221]) #Costo de Venta mercancia
#fi = np.array([3000011, 3790073, 4893892, 5668334, 6267709, 7536174, 13028289, 16371299]) #Gasto de Operación
fi = np.array([7732338, 9609304, 12556893, 16061055, 19101366, 22622597, 28685597, 29973256]) #Utilidad Bruta
#
# planteamos el polinomio de lagrange
n = len(xi)
x = sp.Symbol('x') #representamos a x como simbolo
polin = 0
divL = np.zeros(n, dtype = float)

for i in range(0,n,1):
    
    # creamos los terminos de lagrange
    num = 1
    den = 1
    for j  in range(0,n,1):
        if (j!=i):
            num = num*(x-xi[j])
            den = den*(xi[i]-xi[j])
    trLi = num/den

    polin = polin + trLi*fi[i]
    divL[i] = den

# simplifica el polinomio
pls = polin.expand()
# para evaluación numérica
px = sp.lambdify(x,pls)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

#Evaluar los puntos que se piden
#fr=polin.evalf(subs={x:16})

# SALIDA
print()
print('Polinomio de Lagrange, expresiones')
print(polin)
print()
print('Polinomio de Lagrange: ')
print(pls)
print()
#print("El valor de la función en ese punto es: ", fr)

# Gráfica
plt.plot(pxi,pfi, label = 'Polinomio', color='black')
plt.plot(xi,fi,'o', label = 'Puntos', color = 'purple')
plt.legend()
plt.ylabel('Millones de Pesos')
plt.xlabel('Años')
plt.show()