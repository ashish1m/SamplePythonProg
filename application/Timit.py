import timeit


def power(base, exp):
    return base ** exp


print(timeit.timeit('power(98765, 19)', globals=globals(), number=1000000))
