import random
import time


def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10

    if total > 9:
        total = digit_sum(total)

    return total


sys_time = lambda: time.time() * 1000
start = sys_time()
for _ in range(100000):
    n = random.randint(10000000, 1000000000)
    digit_sum(n)
end = sys_time()
total_time = end - start
print("Time taken: {}ms".format(total_time))
