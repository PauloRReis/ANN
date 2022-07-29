""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.466 e y0=2.389. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.107. """

import numpy as np


def RK4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    l = 0.01337
    u = 0.00851
    r = 0.17159

    def e(t):
        return 1-0.99*np.exp(-0.002*t)

    return r*l*(1-e)

x0, y0 = 0.00134 , 0.788
h=0.0625
n=150
r = RK4(f,x0,y0, h,n)
for xi, yi in r:
    print(xi, yi)