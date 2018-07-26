import unittest
import random
import application.PowerCalc as pc


class PowerCalcTest(unittest.TestCase):

    def test_power(self):
        num = random.randint(1, 100)
        base = random.randint(1, 8)
        result = pc.myPow(num, base)
        self.assertEqual(result, num ** base)


if __name__ == '__main__':
    unittest.main()
