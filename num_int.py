__author__ = 'sandile'
from numbers import*
from numpy import*


def midpoint_rule(f, a, b, n):
    s = 0
    if not isinstance(a, Number):
        raise TypeError("a should be a number")
    elif a is None:
        raise AttributeError("put a value of a")
    elif not isinstance(b, Number):
        raise TypeError("b should be a number")
    elif b is None:
        raise AttributeError("put a value for b")
    elif not isinstance(n, Number):
        raise TypeError("n should be a number")
    elif n is None:
        raise AttributeError("put a value for n")
    else:
        x = linspace(a, b, n+1)
        for i in range(0, n):
            x0 = x[i]
            x1 = x[i+1]
            x_temp = (x1 + x0)/2
            h = f(x_temp)
            s += h*(x1 - x0)
        return s

if __name__ == "__main__":
    def f(x):
        return x**2 - 1
    print("integral:",
          midpoint_rule(f, -2, 2, 10))

if __name__ == "__main__":
    def f(x):
        return x**2 - 1
    print("integral is:",
          midpoint_rule(f, -2, 2, 1000))

    def f(x):
        return 1/x
    print("integral:",
          midpoint_rule(f, 0.1, 2, 100))

    def f(x):
        return x
    print("integral:",
          midpoint_rule(f, 0, 2, 100))


def trapezoidal_rule(f, a, b, n):
    if not isinstance(a, Number):
        raise TypeError("a should be a number")
    elif a is None:
        raise AttributeError("put a value of a")
    elif not isinstance(b, Number):
        raise TypeError("b should be a number")
    elif b is None:
        raise AttributeError("put a value for b")
    elif not isinstance(n, Number):
        raise TypeError("n should be a number")
    elif n is None:
        raise AttributeError("put a value for n")
    else:
        s = 0
        h = (b - a)/n
        s = f(a) + f(b)
        x = linspace(a, b, n + 1)
        for i in range(0, n):
            s += 2*f(x[i + 1])
        return s*h/2
if __name__ == "__main__":

    def f(x):
        return x**2 - 1
    print("integral:",
        trapezoidal_rule(f, -2, 2, 10))

    def f(x):
        return x**2 - 1
    print("integral:",
          trapezoidal_rule(f, -2, 2, 1000))

    def f(x):
        return 1/x
    print("integral:",
          trapezoidal_rule(f, 0.1, 2, 100))

    def f(x):
        return x
    print("integral:",
          trapezoidal_rule(f, -1, 1, 10))


def simpson_rule(f, a, b, n):
    if not isinstance(a, Number):
        raise TypeError("a should be a number")
    elif a is None:
        raise AttributeError("put a value of a")
    elif not isinstance(b, Number):
        raise TypeError("b should be a number")
    elif b is None:
        raise AttributeError("put a value for b")
    elif not isinstance(n, Number):
        raise TypeError("n should be a number")
    elif n is None:
        raise AttributeError("put a value for n")
    else:
        h = (b - a)/(3*n)
        s = f(a) + f(b)
        x = linspace(0, b, n+1)
        g = 0
        for i in range(1, 5):
            x0 = x[2*k - 1]
            x1 = x[2*k - 2]
            x_temp = 4*f(x0) + 2*f(x1)
            return h*(x_temp + s)
if __name__ == "__main__":

    def f(x):
        return x
    print(simpson_rule(f, 0, 2, 5))