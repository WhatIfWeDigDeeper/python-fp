import dis

# Composition
def f(x):
    return x + 2


def g(h, x):
    return h(x) * 2


print(g(f, 42))


# Closures
def addx(x):
    def _(y):
        return x + y
    return _


add2 = addx(2)
add3 = addx(3)

print(add2(2), add3(3))


# Currying
def f(x, y):
    return x*y


def f2(x):
    def _(y):
        return f(x, y)
    return _


print(f2(2))
print(f2(2)(3))

# Single responsibility principle - breaking up fn

# Lambdas in Python


def flambda(x):
    return x.g(lambda x: x.good, lambda x: x.member)


# disassemble function
dis.dis(flambda)


# Lambdas vs Helper functions (more performant)
# avoid premature optimization


