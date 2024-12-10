from __future__ import division
import math
import numpy as np

e = math.e
sin = math.sin
cos = math.cos
ln = np.log

def f(x):
    return e**-x**2 - cos(x)
    # return x**2 + x - 6 #Exercicio1(presenca)

def g(x):
    return -2*x*e**-x**2 + sin(x)
    # return 2*x + 1 # Exercicio1(presenca)

def newton_raphson(f, g, x0, TOL, N):
    x = x0
    for i in range(N):
        fx = f(x)   #função
        gx = g(x)   #derivada

        if abs(gx) < 1e-12:
            raise ValueError("O metodo pode falhar, pois a derivada esta proxima de 0 ")
        
        x1 = x - fx/gx
        erro = abs(x1)

        if abs(x1 - x) < TOL:
            return x1, i, f(x1), erro # retorna a raiz e o numero de iterações
        
        x = x1

    raise ValueError("Número máximo de iterações atingido. O método não convergiu!!!")



x0 = 1.5
TOL = 10**-4
N = 20

raiz, iteracoes, fx, erro = newton_raphson(f, g, x0, TOL, N)
print(f"Raiz: {raiz}")
print(f"Iterações: {iteracoes}")
print(f"f(x): {fx}")
print(f"Erro: {erro}")
