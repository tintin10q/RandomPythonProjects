import unittest


class FibonacciNumberGenerator():
    """Fibonacci number generator class."""

    def __init__(self):
        self.x = 1
        self.y = 0  # 0
        self.n = 0
        self.generator_iter = self.generator()

    def __next__(self):
        return next(self.generator_iter)

    def generator(self):
        """Generator method that yields fibonacci numbers."""
        while True:
            self.n = self.y
            self.y += self.x
            self.x = self.n
            yield self.x


class FibonacciNumberGeneratorUnitTest(unittest.TestCase):
    """Unit test for the fibonacci number generator."""

    def test_number_sequence(self):
        fib = FibonacciNumberGenerator()
        for n in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]:
            self.assertEqual(next(fib), n, 'Generator gave wrong output')

    def test_init(self):
        fib = FibonacciNumberGenerator()
        self.assertEqual(fib.x, 1)
        self.assertEqual(fib.y, 0)
        self.assertEqual(fib.n, 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
