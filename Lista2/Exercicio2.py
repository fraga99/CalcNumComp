from __future__ import division
import math

def f(x):
   return x**3-9*x+5
   #return math.exp(x)-x-2
   #return x*math.log(x,10)-1

def falsa_posicao(f, a, b, TOL, N):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<10}{'Erro':<10}\n")
    for i in range(1, N + 1):
        # Ponto de interseção da reta com o eixo x
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)
        erro = abs(fc)

        # Imprime os dados da iteração
        print(f"{i:<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{fc:<10.6f}{erro:<10.6f}")

        # Verifica se a solução foi encontrada dentro da tolerância
        if erro < TOL:
            print(f"\nConvergiu após {i+1} iterações.")
            return c

        # Atualiza os limites do intervalo
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    raise RuntimeError("Número máximo de iterações alcançado sem convergência.")


falsa_posicao(f, 0, 1, 0.0005, 20)