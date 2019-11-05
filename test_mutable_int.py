import unittest
import faulthandler
from mutable_int import *
import pprint

faulthandler.enable()

y = MutableInt(0)
y.set(4321)
print(y - 210)
print(5432 - y)


class TestMutableInt(unittest.TestCase):

    def test_assign(self):
        y = MutableInt(0)
        id_y = id(y)
        self.assertEqual(y, 0)
        self.assertEqual(0, y)

        y.set(1)
        self.assertTrue(y == 1)
        self.assertTrue(1 == y)
        self.assertEqual(id(y), id_y)

        y.set(6)
        self.assertTrue(y == 6)
        self.assertTrue(6 == y)
        self.assertEqual(id(y), id_y)

        y.set(1024)
        self.assertTrue(y == 1024)
        self.assertTrue(1024 == y)
        self.assertEqual(id(y), id_y)

    def test_math(self):
        y = MutableInt(1234)
        y.set(5678)
        self.assertTrue(y + 1 == 5679)
        self.assertTrue(2 + y == 5680)

        y.set(4321)
        self.assertTrue(y - 210 == 4111)
        self.assertTrue(5432 - y == 1111)

        y.set(6)
        self.assertTrue(y * 2 == 12)
        self.assertTrue(3 * y == 36)

        y.set(10)
        self.assertTrue(y / 2 == 5)
        self.assertTrue(200 / y == 20)



#print(hex(y))
#print(hex(6))
#
#d = {}
#d[y] = 10
#pprint.pprint(d)
#
#print(d[y])
#print(d[6])
#
#print('---')
#a = MutableInt(0)
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#print('---')
#mutable_int_utils.copy_int(a,6)
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#print('---')
#mutable_int_utils.copy_int(a,100000)
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#print('---')
#mutable_int_utils.copy_int(a,-1)
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#print('---')
#mutable_int_utils.copy_int(a,-200)
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#print('---')
#a = 0
#mutable_int_utils.print_int_info(a)
#get_raw(a, 'a')
#b = MutableInt(0)
#mutable_int_utils.print_int_info(b)
#get_raw(b, 'b')
#mutable_int_utils.copy_int(b,a)
#
#print(b+5)
#print(5+b)
#
#mutable_int_utils.print_int_info(b)
#get_raw(b, 'b')
#mutable_int_utils.copy_int(b,-0x87654321)
#mutable_int_utils.print_int_info(b)
#get_raw(b, 'b')
#b.set(0x98765432)
#mutable_int_utils.print_int_info(b)
#get_raw(b, 'b')
#
#print(b+5)
#print(5+b)
#
#print('---')
#c = MutableInt(-10)
##mutable_int_utils.print_int_info(c)
#mutable_int_utils.copy_int(c,-10)
#mutable_int_utils.print_int_info(c)
#get_raw(c, 'c')
#mutable_int_utils.copy_int(c,0)
#mutable_int_utils.print_int_info(c)
#get_raw(c, 'c')
#mutable_int_utils.copy_int(c,1)
#print(c+5)
#print(5+c)
#
#x1 = MutableInt(0)
#x2 = MutableInt(0)
#x3 = MutableInt(0)
#x4 = MutableInt(0)
#x5 = MutableInt(0)
#x6 = MutableInt(0)

if __name__ == '__main__':
    unittest.main()
