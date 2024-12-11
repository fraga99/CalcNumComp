from __future__ import division
import math
e = math.e
cos = math.cos
sin = math.sin


def f(x):
    return e**-x**2 - cos(x)  ## comparação 1
    #return x**3 - x - 1  ## comparação 2
    #return 4*sin(x) - e**x  ## comparação 3
    #return x*log(x) - 1  ## comparação 4 

def secante(f, x0, x1, TOL, N):
    
    print(f"=" * 60)
    i = 0
    while i <= N:
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-12:
            raise ValueError("Divisão por zero. Valores de f(x) próximos.")
                
        if abs(f(x0)) < TOL:
            return fx0
        if abs(f(x1)) < TOL or abs(x1 - x0) < TOL:
            return fx1
        
        x2 = x1 - fx1 * (x1-x0) / (fx1 - fx0)
    
        erro = abs(x2 - x1) / TOL
        
        if abs(x2) < TOL or abs(x2 - x1) < TOL:
            return x2
            
        print(f"Iteração {i + 1}: x = {x2}, f(x) = {f(x2)}, Erro = {erro:}")
    
        x0 = x1
        x1 = x2
            
        i = i + 1
        
        

    raise ValueError("Numero máximo de iterações. Não convergiu!!!")
    


x0 = 1
x1 = 2
TOL = 0.0001                 # tolerância
N = 20                       # iterações


secante(f, x0, x1, TOL, N)
print(f"=" * 60)