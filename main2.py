from solver import *
from math import *
import matplotlib.pyplot as plt

g = 9.81                                    # gravitational Accelaration
l = 1                                       # pendulum length
k = 0                                       # velocity coeff
u0 = 0.5 * pi
du0 = 0
t0 = 0
t_akhir = 4
h = 0.01
w0 = g/l

def Func(t,u,du):
    return -w0 * sin(u) - k*du

res_euler = []
res_eulercromer = []
res_verlet = []
t = []
step = int((t_akhir - t0) / h)

for i in range(step):
    tm = (i + 1) * h
    (u_next, du_next) = euler(tm, h, u0, du0, Func)
    res_euler.append(u_next)
    t.append(tm)
    u0 = u_next
    du0 = du_next

t = []
u0 = 0.5 * pi
du0 = 0
d2u0 = Func(t0,u0,du0)

for i in range(step):
    tm = (i + 1) * h
    (u_next, du_next) = euler_cromer(tm, h, u0, du0, Func)
    res_eulercromer.append(u_next)
    t.append(tm)
    u0 = u_next
    du0 = du_next

t = []
u0 = 0.5 * pi
du0 = 0
d2u0 = Func(t0,u0,du0)

for i in range(step):
    tm = (i + 1) * h
    (u_next, du_next,d2u_next) = verlet(tm, h, u0, du0, d2u0, Func)
    res_verlet.append(u_next)
    t.append(tm)
    u0 = u_next
    du0 = du_next
    d2u0 = d2u_next

plt.title('Non Linear Pendulum h =0.01')
plt.plot(t,res_euler,color='r', label = 'Euler')
plt.plot(t,res_eulercromer,color='g', label = 'Euler Cromer')
plt.plot(t,res_verlet,color='b', label = 'Verlet')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()

plt.show()



