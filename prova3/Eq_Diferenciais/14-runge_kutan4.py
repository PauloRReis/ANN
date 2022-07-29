import math

def RK4(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        m3 = f(x0 + (h/2), y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        yield[x0, y0]
    
# modificar valores de r e lambd    
def f(p, t):
    r = 0.17159
    lambd = 0.01337
    k = r * lambd
    return k * (1 - t)

# modificar valor de p0    
t0 = 0
p0 = 0.00134
h = 1
n = 150

r = RK4(f, t0, p0, h, n)

runge = []
for yi in r:
    runge.append(yi[1])
    
# solução exata:
# modificar valores de r, lambd e coef 
def p(t):
    r = 0.17159
    lambd = 0.01337
    k = r * lambd
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao
    coef = 0.99866
    return 1 - coef * math.exp(-k*t)
    
for i in range(150):
    print(f"{runge[i]}, {abs(runge[i] - p(i))},")