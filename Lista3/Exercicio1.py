from __future__ import division
import math
#import numpy as np

e = math.e
sin = math.sin
cos = math.cos
log = math.log

def f(x):
    return e**-x**2 - cos(x)  ## comparação 1
    #return x**3 - x - 1  ## comparação 2
    #return 4*sin(x) - e**x  ## comparação 3
    #return x*log(x) - 1  ## comparação 4

def g(x):
    return -2*x*e**-x**2 + sin(x)  ## comparação 1  (derivado)
    #return 3*x**2 - 1  ## comparação 2  (derivado)
    #return 4*sin(x) - e**x  ## comparação 3
    #return x*log(x) - 1  ## comparação 4

def newton_raphson(f, g, x0, TOL, N):
    x = x0
    x_anterior = x0
    for i in range(N):
        fx = f(x)   #função
        gx = g(x)   #derivada

        if abs(gx) < 1e-12:
            # ("O metodo pode falhar, pois a derivada esta proxima de 0 ")`
            raise ValueError("O metodo pode falhar, pois a derivada esta proxima de 0 ")
        
        x1 = x - fx/gx
        erro = abs(x1 - x)

        if abs(f(x1)) < TOL:
            return x1, i, f(x1), erro # retorna a raiz e o numero de iterações
        if abs(x1 - x0) < TOL:
            return x1, i, f(x1), erro # retorna a raiz e o numero de iterações
            
        x = x1

    raise ValueError("Número máximo de iterações atingido. O método não convergiu!!!")



x0 = 1.5
TOL = 10**-4
N = 20

raiz, iteracoes, fx, erro = newton_raphson(f, g, x0, TOL, N)
print(f"\nIterações: {iteracoes}")
print(f"x: {raiz}")
print(f"f(x): {fx}")
print(f"Erro: {erro:.7f}\n")

