import time
import random
import timeit


def myPow(base, exp):
    if exp == 1:
        return base
    else:
        return base * myPow(base, exp - 1)


print(timeit.timeit('myPow(98765, 19)', globals=globals(), number=1000000))
