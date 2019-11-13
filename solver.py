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