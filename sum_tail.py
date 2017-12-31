# Python doesn't support tail call optimization
def s(n, acc=0):
    if n == 0:
        return acc
    else:
        return s(n-1, acc+n)


print(s(10))


# Trampolining with Generators

def fib(n, cur=0, nxt=1):
    if n == 0:
        return cur
    else:
        return fib(n - 1, nxt, cur + nxt)


print([fib(i) for i in range(10)])


