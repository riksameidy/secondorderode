from solver import *

def cauchy_euler(params,Func):
    # Initial Condition
    t0 = params['t0']
    t_akhir = params['t_akhir']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']

    res_euler = []
    t = []
    step = int((t_akhir - t0) / h)

    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = euler(tm, h, y0, dy0, Func)
        res_euler.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next

    return (t,res_euler)

def cauchy_eulercromer(params,Func):
    # Initial Condition
    t0 = params['t0']
    t_akhir = params['t_akhir']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']

    res_euler_cromer = []
    t = []
    step = int((t_akhir - t0) / h)

    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = euler_cromer(tm, h, y0, dy0, Func)
        res_euler_cromer.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next
    return (t, res_euler_cromer)