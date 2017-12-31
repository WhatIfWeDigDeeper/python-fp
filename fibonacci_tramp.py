from tramp import tramp


def fib(n, curr=0, nxt=1):
    if n == 0:
        yield curr
    else:
        yield fib(n - 1, nxt, curr + nxt)


print([tramp(fib, i) for i in range(10)])

print(tramp(fib, 1000))
