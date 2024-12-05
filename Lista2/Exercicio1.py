from __future__ import division
import math

def f(x):
   return x**3-9*x+5
   #return math.exp(x)-x-2
   #return x*math.log(x,10)-1

def bisseccao(f, a, b, TOL, N):
      
   if f(a) * f(b) >= 0:
    raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
   
   print(f"{'Iteração':<10}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<10}{'Erro':<10}\n")
   
   for i in range(N):
      c = (a + b) / 2  # Ponto médio do intervalo
      fc = f(c)
      erro = abs(fc)

      print(f"{i:<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{fc:<10.6f}{erro:<10.6f}")


      if abs(fc) < TOL or (b - a) / 2 < TOL:
         print('\n')
         print(f"Convergiu após {i + 1} iterações.")
         return c

      if f(a) * fc < 0:
         b = c  # A raiz está no intervalo [a, c]
      else:
         a = c  # A raiz está no intervalo [c, b]

   raise RuntimeError("Número máximo de iterações alcançado sem convergência.")



raiz = bisseccao(f, 0, 1, 0.001, 20)
print (f"A raiz encontrada é: {raiz}");