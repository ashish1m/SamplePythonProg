import time
import random
import timeit


def calc_pow(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1

    if exp % 2 == 0:
        half_exp = exp / 2
        temp_half_res = calc_pow(base, half_exp)
        return temp_half_res * temp_half_res
    else:
        half_exp = int((exp // 2))
        temp_half_res = calc_pow(base, half_exp)
        return base * temp_half_res * temp_half_res


def calc_exp(base, exp):
    if exp < 0:
        return 1 / calc_pow(base, abs(exp))
    elif 0 < exp < 1:
        return "Not handled yet"
    else:
        return calc_pow(base, exp)


def calc_pow_for(base, exp):
    MOD = 1000000007
    power = 1
    for i in range(exp):
        power = (power * base) % MOD

    return power


# base = float(input("Enter the base: "))
# exp = float(input("Enter the exp: "))
#
# print(calc_exp(base, exp))

print(timeit.timeit('calc_exp(98765, 19)', globals=globals(), number=1000000))
