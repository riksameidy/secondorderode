from solver import *
from math import *
import matplotlib.pyplot as plt

# params
g = 9.81
m = 7
k = 0.01
x0 = 0.0
y0 = 3.0
vx0 = 20.0
vy0 = 20.0
ax0 = 0
ay0=0
t_akhir = 20
t0 = 0
h = 0.001

def Forces(m,x,y,vx,vy,k):
    fx = -k * vx * abs(vx)
    fy = -k * vy * abs(vy) - m*g
    Epot = m * g * h
    return (fx,fy,Epot)

t = []
res = []
res2 = []
res3 = []
step = int((t_akhir - t0) / h)
i=0
while (i < step and y0>0):
    tm = (i + 1) * h
    (rx_next,ry_next,vx_next,vy_next,ax_next,ay_next,Ekin,Epot) = verlet2DNewton(m ,h,x0,y0, vx0, vy0 , ax0, ay0, Forces,k=0.00)
    res.append((rx_next,ry_next))
    t.append(tm)

    x0 = rx_next
    y0 = ry_next
    vx0 = vx_next
    vy0 = vy_next
    ax0 = ax_next
    ay0 = ay_next
    i = i+1

# params
g = 9.81
m = 7
k = 0.01
x0 = 0.0
y0 = 3.0
vx0 = 20.0
vy0 = 20.0
ax0 = 0
ay0=0
t_akhir = 20
t0 = 0
h = 0.001
i=0
while (i < step and y0>0):
    tm = (i + 1) * h
    (rx_next,ry_next,vx_next,vy_next,ax_next,ay_next,Ekin,Epot) = verlet2DNewton(m ,h,x0,y0, vx0, vy0 , ax0, ay0, Forces,k=0.01)
    res2.append((rx_next,ry_next))
    t.append(tm)

    x0 = rx_next
    y0 = ry_next
    vx0 = vx_next
    vy0 = vy_next
    ax0 = ax_next
    ay0 = ay_next

# params
g = 9.81
m = 7
k = 0.01
x0 = 0.0
y0 = 3.0
vx0 = 20.0
vy0 = 20.0
ax0 = 0
ay0=0
t_akhir = 20
t0 = 0
h = 0.001
i=0
while (i < step and y0>0):
    tm = (i + 1) * h
    (rx_next,ry_next,vx_next,vy_next,ax_next,ay_next,Ekin,Epot) = verlet2DNewton(m ,h,x0,y0, vx0, vy0 , ax0, ay0, Forces,k=0.02)
    res3.append((rx_next,ry_next))
    t.append(tm)

    x0 = rx_next
    y0 = ry_next
    vx0 = vx_next
    vy0 = vy_next
    ax0 = ax_next
    ay0 = ay_next

x_ = [ el[0] for el in res]
y_ = [ el[1] for el in res]
plt.title('trajectory')
plt.plot(x_,y_,color='b', label = 'k = 0.00')
x_ = [ el[0] for el in res2]
y_ = [ el[1] for el in res2]
plt.plot(x_,y_,color='g', label = 'k = 0.01')
x_ = [ el[0] for el in res3]
y_ = [ el[1] for el in res3]
plt.plot(x_,y_,color='r', label = 'k = 0.02')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()