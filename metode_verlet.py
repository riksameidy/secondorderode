from solver import *

def cauchy_verlet(params,Func):
    # Initial Condition
    t0 = params['t0']
    t_akhir = params['t_akhir']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']

    res_verlet = []
    t = []
    step = int((t_akhir - t0) / h)

    d2y0 = Func(t0,y0,dy0)
    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next, d2y_next) =  verlet(tm,h,y0,dy0,d2y0,Func)
        res_verlet.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next
        d2y0 = d2y_next
    return (t, res_verlet)