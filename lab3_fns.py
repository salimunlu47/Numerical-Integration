# File: lab3_fns.py
# This file contains definitions of the functions used in the lab.

import math
import sys

def test_fn(x):
    return x
    
# the example from Stein pp.370-372
def f0(x):
    return 1.0/(1.0 + x*x)

def f1(x):
    return 1.0/math.sqrt(x*x-9.0)

def f2(x):
    return (1.0/math.sqrt(2*math.pi))*math.exp(-math.pow(x,2)/2)

def f3(x, y):
    return x**2+y

def rectangular(f, a, b, n):
    h=float(b-a)/n
    s=0.0
    i=1
    while i<=n:
        x=a+i*h
        s=s+f(x)
        i=i+1
    return h*s
    
def trapezoidal(f, a, b, n):
    h=float(b-a)/n
    s=0.0
    i=0
    while i<=n:
        x=a+i*h
        if (i==0) or (i==n):
            s=s+f(x)
        else:
            s=s+2*f(x)
        i=i+1
    return (h/2)*s

def simpsons(f, a, b, n):
    h=float(b-a)/n
    s=0.0
    i=0
    while i<=n:
        x=a+i*h
        if (i==0) or (i==n):
            s=s+f(x)
        elif (i%2==0):
            s=s+2*f(x)
        else:
            s=s+4*f(x)
        i=i+1
    return (h/3)*s
    
def rect2d(f, ax, bx, nx, ay, by, ny):
    hx=float(bx-ax)/nx
    hy=float(by-ay)/ny
    hA=hx*hy
    s=0.0
    i=1
    while i<=nx:
        j=1
        while j<=ny:        
            x=ax+i*hx
            y=ay+j*hy
            s=s+f(x,y)
            j=j+1
        i=i+1
    return hA*s
    
def integral(method, f):
    n=10
    while n<=1000:
        result=method(f, 4, 5, n)
        val1=math.log(9/(4+math.sqrt(7)))
        error=abs(result-val1)
        print ('segment: %-4d' % n,)
        print ('result: %.12f' % result,)
        print ('abs error: %.12f' % error)
        n=n*10