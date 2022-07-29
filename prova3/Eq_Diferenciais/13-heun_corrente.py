import numpy as np
import matplotlib.pyplot as plt


def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return -y/np.sqrt(9**2-y**2)


def g(t, i):
    c = 0.2041
    r = 1.0748 
    l = 1.5355

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0598

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.0715
    n = 150
    b = 1/2
    x_values =  [0.0648, 0.1175, 0.2261, 0.375, 0.4872, 0.5183, 0.6595, 0.7117, 0.8516, 0.9596, 1.0172, 1.1876, 1.2628, 1.3154, 1.417, 1.5412, 1.6214, 1.755, 1.8528, 1.9143, 2.0538, 2.1833, 2.2797, 2.3288, 2.4345, 2.5193, 2.6307, 2.7535, 2.8713, 2.933, 3.0438, 3.1787, 3.2854, 3.3175, 3.4887, 3.5324, 3.6742, 3.7553, 3.8607, 3.9716, 4.01, 4.1656, 4.2497, 4.32, 4.4485, 4.5244, 4.6186, 4.7586, 4.8119, 4.9132, 5.0549, 5.1897, 5.2228, 5.3174, 5.4529, 5.5548, 5.647, 5.7602, 5.8888, 5.9513, 6.0321, 6.136, 6.2253, 6.3404, 6.4606, 6.5882, 6.6157, 6.7524, 6.8504, 6.9501, 7.0688, 7.1286, 7.2417, 7.3832, 7.4854, 7.5626, 7.6433, 7.7521, 7.8293, 7.9751, 8.0864, 8.1269, 8.2262, 8.3738, 8.4229, 8.5204, 8.6869, 8.7381, 8.8289, 8.9611, 9.0638, 9.1568, 9.2314, 9.3623, 9.4716, 9.5565, 9.6132, 9.7744, 9.8211, 9.9152, 10.0825, 10.1214, 10.2539, 10.3157, 10.4723, 10.5828, 10.6662, 10.7508, 10.8258, 10.9563, 11.0411, 11.135, 11.2663, 11.3316, 11.4615, 11.53, 11.6592, 11.7115, 11.8108, 11.9509, 12.0746, 12.1564, 12.2298, 12.3131, 12.4469, 12.5828, 12.6148, 12.7898, 12.8576, 12.9283, 13.0607, 13.1553, 13.2437, 13.3565, 13.4642, 13.5569, 13.6569, 13.7199, 13.8178, 13.9163, 14.0753, 14.1745, 14.2876, 14.3109, 14.4887, 14.5562, 14.6685, 14.7736, 14.822, 14.9253]

    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2_h_variavel(g, x0, y0, n, b, x_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')