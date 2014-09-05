__author__ = 'sandile'
from numbers import*
from numpy import*

def secant(f, x1, x0, e):
    if f(x1) - f(x0) == 0:
        return x1
    while abs(f(x1)) > e:
        x_temp = x1 - (f(x1)*(x1-x0)*1.0/(f(x1)-f(x0)))
        x0 = x1
        x1 = x_temp
        if not isinstance(x1, Number):
            raise TypeError("x1 should be a number")
        elif x1 is None:
            raise AttributeError("put a value of x1")
        elif not isinstance(x0, Number):
            raise TypeError("x0 should be a number")
        elif x0 is None:
            raise AttributeError("put a value for x0")
        elif not isinstance(e, Number):
            raise TypeError("e should be a number")
        elif e is None:
            raise AttributeError("put a value for e")
        else:
            return x1
if __name__ == "__main__":
    def f(x):
        return sin(x) + cos(x)
    print("root is:",
          secant(f, pi/2, 3*pi/2, 1e-6))

    def f(x):
        return sin(x) + cos(x)
    print("root is:",
          secant(f, -pi/2, pi/2, 1e-6))

    def f(x):
        return x**3
    print("root is:",
          secant(f, 5, 6, 1e-9))

    def f(x):
        return x
    print("root is:",
          secant(f, -1, 1, 0.0001))