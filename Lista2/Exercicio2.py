from __future__ import division
import math
e = math.e
sin = math.sin
log = math.log10

def f(x):
   return x**3-9*x+5 

def falsa_posicao(f, a, b, TOL, N):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'x':<10}{'f(x)':<10}{'Erro':<10}\n")

    for i in range(1, N + 1):
        # Ponto de interseção da reta com o eixo x
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fx = f(x)
        erro = abs(fx)

        # Imprime os dados da iteração
        print(f"{i:<10}{a:<10.6f}{b:<10.6f}{x:<10.6f}{fx:<10.6f}{erro:<10.6f}")

        # Verifica se a solução foi encontrada dentro da tolerância
        if erro < TOL:
            print(f"\nConvergiu após {i+1} iterações.")
            print(f"Intervalo final: [{+a:.6f}, {b:.6f}]")
            print(f"x = {x:.6f}")
            print(f"f(x) = {fx:.6f}")
            return x

        # Atualiza os limites do intervalo
        if f(a) * fx < 0:
            b = x
        else:
            a = x

    raise RuntimeError("Número máximo de iterações alcançado sem convergência.")

N = 20
a = 0
b = 1
TOL = 0.0005

falsa_posicao(f, a, b, TOL, N)