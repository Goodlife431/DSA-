import unittest


def multiply_numbers(a, b):
    count = 0
    for num in range(b):
        count += a
    return count


num1 = 5
num2 = 3
result = multiply_numbers(num1, num2)


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply_numbers(5, 3), 15)


if __name__ == '__main__':
    unittest.main()
