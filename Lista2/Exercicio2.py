from __future__ import division
import math
e = math.e
sin = math.sin
log = math.log10
cos = math.cos

def f(x):
    return e**-x**2 - cos(x)  ## comparação 1
    #return x**3 - x - 1  ## comparação 2
    #return 4*sin(x) - e**x  ## comparação 3
    #return x*log(x) - 1  ## comparação 4 

def falsa_posicao(f, a, b, TOL, N):
    if f(a) * f(b) > 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'x':<10}{'f(x)':<10}{'Erro':<10}")
    print(f"-" * 60)
    
    i = 0
    while i < N:
        # Ponto de interseção da reta com o eixo x
        x = ((a * f(b) - b * f(a)) / (f(b) - f(a)))
        fx = f(x)
        M = f(a)
        erro = abs(b-a)

        # Imprime os dados da iteração
        print(f"{i:<10}{a:<10.6f}{b:<10.6f}{x:<10.6f}{fx:<10.6f}{erro:6f}")        
        
        # Atualiza os limites do intervalo
        if (b-a) < TOL:
            if abs(f(a)) < TOL:
                a = x
            if abs(f(b)) < TOL:
                b = x
        
        
        
        if abs(fx) < TOL or erro < TOL:
            print(f"\nNumero de iterações: {i + 1}")
            print(f"Intervalo final: [{a}, {b}]")
            print(f"x = {x}")
            print(f"f(x) = {fx}")
            print(f"Erro em x = {erro}")
            return x
        
        if M*f(x) < 0:
            b = x
        else:
            a = x
            
        i = i + 1
    raise RuntimeError("Número máximo de iterações alcançado sem convergência.")

N = 30
a = 1
b = 2
TOL = 0.0001

falsa_posicao(f, a, b, TOL, N)