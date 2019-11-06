import unittest
import mutable_int
from mutable_int import *
import pprint
import copy

class TestMutableInt(unittest.TestCase):

    def test_assign(self):
        y = MutableInt(0)
        id_y = id(y)
        self.assertEqual(y, 0)
        self.assertEqual(0, y)

        y.set(1)
        self.assertEqual(y, 1)
        self.assertEqual(1, y)
        self.assertEqual(id(y), id_y)

        y.set(6)
        self.assertEqual(y, 6)
        self.assertEqual(6, y)
        self.assertEqual(id(y), id_y)

        y.set(1024)
        self.assertEqual(y, 1024)
        self.assertEqual(1024,  y)
        self.assertEqual(id(y), id_y)

        y.set(0xff123456)
        self.assertEqual(y, 0xff123456)
        self.assertEqual(0xff123456, y)
        self.assertEqual(id(y), id_y)

        y.set(-9876)
        self.assertEqual(y, -9876)
        self.assertEqual(-9876, y)
        self.assertEqual(id(y), id_y)

        a = MutableInt(100)
        b = MutableInt(100)
        self.assertNotEqual(id(a), id(b))

    def test_math(self):
        y = MutableInt(1234)
        y.set(5678)
        self.assertEqual(y + 1, 5679)
        self.assertEqual(2 + y, 5680)

        y.set(4321)
        self.assertEqual(y - 210, 4111)
        self.assertEqual(5432 - y, 1111)

        y.set(6)
        self.assertTrue(y * 2 == 12)
        self.assertTrue(3 * y == 18)

        y.set(10)
        self.assertTrue(y / 2 == 5)
        self.assertTrue(200 / y == 20)

        y.set(2)
        self.assertTrue(5 ** y == 25)
        self.assertTrue(y ** 5 == 32)

    def test_convert(self):
        x = 0xFF1234
        y = MutableInt(x)
        self.assertEqual(hex(x), hex(y))
        self.assertEqual(hex(y), hex(x))
        self.assertEqual(str(x), str(y))
        self.assertEqual(str(y), str(x))
        self.assertIs(int(y), x)
        self.assertIs(x, int(y))

    def test_dict(self):
        d = {}
        d[50] = 'hello'
        d[51] = 'world'
        y = MutableInt(1)
        y.set(50)
        self.assertEqual('hello', d[y])
        y.set(51)
        self.assertEqual('world', d[y])
        y.set(151)
        d[y] = 'python'
        self.assertEqual('python', d[151])

        MutableInt.use_id_for_hash = True

        with self.assertRaises(KeyError):
            d[y]

        x = MutableInt(999)
        d[x] = 'pycon'
        x.set(1001)
        self.assertEqual('pycon', d[x])

        MutableInt.use_id_for_hash = False

    def test_copy(self):
        y = MutableInt(1214)
        y.x = MutableInt(999)

        a = copy.copy(y)
        self.assertEqual(a, y)
        self.assertNotEqual(id(a), id(y))
        self.assertEqual(id(a.x), id(y.x))

        y.set(2451)
        b = copy.deepcopy(y)
        self.assertEqual(b, y)
        self.assertNotEqual(a, b)
        self.assertNotEqual(id(b), id(y))
        self.assertNotEqual(id(b.x), id(y.x))



if __name__ == '__main__':
    unittest.main()
