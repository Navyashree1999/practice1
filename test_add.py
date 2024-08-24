import unittest
from example import addition

class AdditionTest(unittest.TestCase):
    def test_addition(self):
        self.assertEquals(addition(10,20),30)


if __name__ == '__main__':
    unittest.main()
