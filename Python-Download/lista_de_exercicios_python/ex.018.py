import math
ag = float(input('Digite um ângulo: '))
s = math.sin(math.radians(ag))
c = math.cos(math.radians(ag))
t = math.tan(math.radians(ag))
print('O seno do ângulo de {:.0f}º é: {:.1f}\nO cosseno do ângulo de {:.0f}º é {:.1f}\nA tangente do ângulo de {:.0f} é: {:.1f}\n'
      .format(ag, s, ag, c, ag, t))