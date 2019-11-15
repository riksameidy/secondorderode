def euler(t,h,y,dy,Func):
    d2y = Func(t,y,dy)
    y_next = y + (h * dy)
    dy_next = dy + (h * d2y)
    return ( y_next, dy_next )

def euler_cromer(t,h,y,dy,Func):
    d2y = Func(t, y, dy)
    dy_next = dy + (h * d2y)
    y_next = y + (h * dy_next)

    return (y_next, dy_next)

def verlet(t,h,y,dy,d2y,Func):
    h1_2 = 0.5 * h
    dy1_2 = dy + (h1_2 * d2y)
    y_next = y + (h * dy1_2)

    d2y_next = Func(t,y_next,dy1_2)
    dy_next = dy1_2 + (h1_2 * d2y_next)
    return (y_next,dy_next,d2y_next)

def verlet2DNewton(m ,h,rx,ry, vx, vy , ax, ay, Forces,k):
    h1_2 = 0.5 * h
    vx1_2 = vx + (h1_2 * ax) ; vy1_2 = vy + (h1_2 * ay)
    rx_next = rx + (h * vx1_2) ; ry_next = ry + (h * vy1_2)

    (fx,fy,Epot) = Forces(m,rx_next,ry_next,vx1_2,vy1_2,k)
    ax_next = fx/m ; ay_next = fy/m

    vx_next = vx1_2 + (h1_2 * ax_next) ; vy_next = vy1_2 + (h1_2 * ay_next)

    Ekin = 1/2 * m * (vx**2 + vy**2)

    return (rx_next,ry_next,vx_next,vy_next,ax_next,ay_next,Ekin,Epot)