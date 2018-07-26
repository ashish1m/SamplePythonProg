import random
import time


class RandomNumGen:

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def get_random(self):
        random.seed(time.time())
        return int(random.random() * (self.high - self.low)) + self.low


r = RandomNumGen(5, 25)
print(r.get_random())
