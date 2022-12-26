import unittest
from main import fibonacci
import unittest
import main

def test_1():
    assert (list(main.fibonacci(3)) == [0, 1, 1])

def test_2():
    assert (list(fibonacci(4)) == [0, 1, 1, 2])

def test_3():
    assert (list(fibonacci(5)) == [0, 1, 1, 2, 3])


class TestEquation(unittest.TestCase):

    def test_get_roots(self):
        self.assertEqual(list(fibonacci(5)),[0, 1, 1, 2, 3])

    def test_value(self):
        self.assertEqual(list(fibonacci(7)),[0, 1, 1, 2, 3,5,8])

    def test_type(self):
        (self.assertRaises(TypeError),fibonacci("A"),("Введено не число"))


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    unittest.main()
