from __future__ import division
import math
e = math.e
cos = math.cos
sin = math.sin
log = math.log10


def f(x):
   #return e**-x**2 - cos(x)  ## comparação 1
   #return x**3 - x - 1  ## comparação 2
   return 4*sin(x) - e**x  ## comparação 3
   #return x*log(x) - 1  ## comparação 4


def bisseccao(f, a, b, TOL, N):

   if f(a) * f(b) > 0:
      raise ValueError("A função deve ter sinais opostos nos pontos a e b.")

   print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'c':<10}{'f(x)':<10}{'erro':<10}")
   print(f"-" * 60)
   i = 0
   while i <= N:
      M = f(a)
      x = (a + b) / 2  # Ponto médio do intervalo
      fx = f(x)
      erro = abs(b - a)/2

      print(f"{i:<10}{a:<10.6f}{b:<10.6f}{x:<10.6f}{fx:<10.6f}{erro:<10.6f}")

      if M * f(x) < 0:
         b = x  # A raiz está no intervalo [a, c]
      else:
         a = x  # A raiz está no intervalo [c, b]

      if (b-a) < TOL:
         print('\n')
         print(f"Numero de iterações: {i + 1}")
         print(f"Intervalo final: [{a}, {b}]")
         print(f"x = {x}")
         print(f"f(x) = {f(x)}")
         print(f"erro em x: {erro}\n")
         return x
      
      i += 1
   raise RuntimeError("Número máximo de iterações alcançado sem convergência.")

N = 30
TOL = 0.00001
a = 0
b = 1

bisseccao(f, a, b, TOL, N)

