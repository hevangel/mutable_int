import faulthandler
faulthandler.enable()
import mutable_int_utils
from mutable_int import *
import atexit
import pprint

class MutableIntBase():
    """ Base class of mutable integer type to override the hash() function"""
    def __new__(cls, val, maxval=0xFFFFFFFF):
        return int.__new__(cls, maxval)


class MyInt(MutableIntBase, int):
    """ Base class of mutable integer type to override the hash() function"""
    #def __new__(cls, val, maxval=0xFFFFFFFF):
    #    return int.__new__(cls, maxval)

    def __init__(self, val, maxval=0xFFFFFFFF):
        self.val = val
        self.maxval = maxval
        mutable_int_utils.copy_int(self,val)
        #atexit.register(mutable_int_utils.copy_int,self,1)

    def __int__(self):
        return self.val

    def __index__(self):
        return int(self)

    def __hash__(self):
        return int(self)

    def __iter__(self):
        return iter([self])

    def __eq__(self, other):
        return int(self) == other

    def set(self, val):
        # Check the new value is a integer type
        assert isinstance(val, int)

        # Check the new value is smaller than the maxval (pre-allocated memory size)
        assert (val >= 0 and val <= self.maxval)

        mutable_int_utils.copy_int(self,val)

y = MyInt(0)
mutable_int_utils.copy_int(y,1)
mutable_int_utils.copy_int(y,6)
mutable_int_utils.copy_int(y,0)

a = 0

if y == a:
    print('yes')
else:
    print('no')

if a == y:
    print('yes')
else:
    print('no')


mutable_int_utils.copy_int(y,6)
print(hex(y))
print(hex(6))

d = {}
d[y] = 10
pprint.pprint(d)

print(d[y])
print(d[6])

#print('---')
#a = MyInt(0)
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
#b = MyInt(0)
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
#c = MyInt(-10)
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
#x1 = MyInt(0)
#x2 = MyInt(0)
#x3 = MyInt(0)
#x4 = MyInt(0)
#x5 = MyInt(0)
#x6 = MyInt(0)

