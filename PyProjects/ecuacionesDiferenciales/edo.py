import numpy as np


def yprima(x,y):
    #return(-3*x)+(2*y)-5
    return 2*np.e**x*np.cos(y)

def euler(x, y, h):
    yp1=y+(h*yprima(x,y))
    return yp1

def rungekutta2(x, y, h):
    k1=yprima(x,y)
    k2=yprima(x+(0.5*h),y+(0.5*k1*h))
    yp1=y+(k2*h)
    return yp1

def rungekutta3(x, y, h):
    k1=yprima(x,y)
    k2=yprima(x+(0.5*h),y+(0.5*k1*h))
    k3=yprima(x+h, y-(k1*h)+(2*k2*h))
    yp1=y+((k1+(4*k2)+k3)/6*h)
    return yp1

def rungekutta4(x, y, h):
    k1=yprima(x, y)
    k2=yprima(x+(0.5*h),y+(0.5*k1*h))
    k3=yprima(x+(0.5*h),y+(0.5*k2*h))
    k4=yprima(x+h,y+(h*k3))
    yp1=y+((h/6)*(k1+(2*k2)+(2*k3)+k4))
    return yp1

def rungekutta5(x, y, h):
    k1=yprima(x, y)
    k2=yprima(x+(0.25*h),y+(0.25*k1*h))
    k3=yprima(x+(0.25*h),y+(0.125*k1*h)+(0.125*k2*h))
    k4=yprima(x+(0.5*h),y-(0.5*k2*h)+k3*h)
    k5=yprima(x + (0.75*h), y + (0.1875*k1*h) + (0.5625*k4*h))
    k6=yprima(x + h,y - (3/7*k1*h) + (2/7*k2*h) + (12/7*k3*h) - (12/7*k4*h) + (8/7*k3*h))
    ypp1=y+(1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*h)
    return ypp1