from __future__ import division
import math
e = math.e

def f(x):
   return x**3-9*x+5 


def bisseccao(f, a, b, TOL, N):

   if f(a) * f(b) > 0:
    raise ValueError("A função deve ter sinais opostos nos pontos a e b.")

   print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'c':<10}{'f(x)':<10}{'Erro':<10}\n")

   i = 0
   while i <= N:
      M = f(a)
      x = (a + b) / 2  # Ponto médio do intervalo
      fx = f(x)
      erro = abs(fx)

      print(f"{i:<10}{a:<10.6f}{b:<10.6f}{x:<10.6f}{fx:<10.6f}{erro:<10.6f}")


      if abs(fx) < TOL or (b - a) / 2 < TOL:
         print('\n')
         print(f"Convergiu após {i + 1} iterações.")
         print(f"Intervalo final: [{+a:.6f}, {b:.6f}]")
         print(f"x = {x:.6f}")
         print(f"f(x) = {fx:.6f}")
         return x

      if M * fx > 0:
         a = x  # A raiz está no intervalo [a, c]
      else:
         b = x  # A raiz está no intervalo [c, b]

      i += 1
   raise RuntimeError("Número máximo de iterações alcançado sem convergência.")

N = 20
a = 0
b = 1
TOL = 0.001
bisseccao(f, a, b, TOL, N)
