import unittest


def foo(n):
    return n+1


class FooTest(unittest.TestCase):
    def test_foo(self):
        r = foo(10)
        self.assertEqual(r, 12)

assert(foo(10) == 12)
