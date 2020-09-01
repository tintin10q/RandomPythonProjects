import unittest


class FibonacciNumberGenerator():
    def __init__(self):
        self.x = 1
        self.y = 0  # 0
        self.n = 0
        self.generator_iter = self.generator()

    def __next__(self):
        return next(self.generator_iter)

    def generator(self):
        while True:
            self.n = self.y
            self.y += self.x
            self.x = self.n
            yield self.x


fib = FibonacciNumberGenerator()

for i in range(10):
    print(next(fib))


class FibonacciNumberGeneratorUnitTest(unittest.TestCase):

    def test_number_sequence(self):
        """ Test fibonacci generator up till n = 10 """
        fib = FibonacciNumberGenerator()
        correct_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for n in range(10):
            self.assertEqual(next(fib), correct_sequence[n], 'Generator gave wrong output at n={n}'.format(n=n))

    def test_init(self):
        """ Test init values """
        fib = FibonacciNumberGenerator()
        self.assertEqual(fib.x, 1)
        self.assertEqual(fib.y, 0)
        self.assertEqual(fib.n, 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
