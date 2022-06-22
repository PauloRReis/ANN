import math
import trapezio as trapz
from numpy import double

def interval(x1, x2):
    def f(x):
        return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)
# Variável inferior
    a = [0.56, 1.1, 2.195, 2.604, 3.073, 3.883, 3.905]
# Variável superior
    b = [2.876, 2.724, 2.038, 2.357, 2.913, 1.607, 1.532]
    n = interval()
    r = trapz(f, a, b, n)
    
