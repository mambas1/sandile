for i in range(1, 5):
        s += 4*f(x[2*i - 1])
        v += 2*f(x[2*i - 2])
    return l + h + s + v
if __name__ == "__main__":

    def f(x):
        return x
    print(simpson_rule(f, 0, 2, 10))