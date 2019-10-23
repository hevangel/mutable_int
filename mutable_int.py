import sys
import ctypes

def get_raw(obj, s = None):
    if (s is None):
        s = str(obj)
    print('get_raw(',s,'): id()', id(obj));
    print('int()', int(obj))
    print('str()', str(obj))
    print('repr()', repr(obj))
    print('getsizeof:', sys.getsizeof(obj))
    print('hash:', hash(obj))
    ob_size = ctypes.c_short.from_address(id(obj)+16)
    print('ob_size:', ob_size.value)
    for i in range(abs(ob_size.value)):
        ob_digit = ctypes.c_long.from_address(id(obj)+24+i*4)
        digit = int(ob_digit.value) & 0x3FFFFFFF
        print('ob_digi[', i,']', hex(digit))

class MutableIntBase():
    """ Base class of mutable integer type to override the hash() function"""
    def __new__(cls, val, maxval=0xFFFFFFFF):
        return int.__new__(cls, maxval)

    def __init__(self, val = 0):
        self._val = val

    #def __int__(self):
    #    return self._val

    #def __index__(self):
    #    return self._val

    #def __str__(self):
    #    return str(self._val)

    #def __repr__(self):
    #    return repr(self._val)

    #def __iter__(self):
    #    return iter([self])


#class MutableInt(int):
class MutableInt(MutableIntBase, int):
    """ Mutable integer type"""

    def __init__(self, val, maxval=0xFFFFFFFF):
        self.maxval = maxval
        print('--- val: ', val, '---')
        self.set(val)

    def __hash__(self):
        return id(self)

    def __iter__(self):
        return iter([self])

    def set(self, val):
        # Copy the raw memory value of the integer from the C data structure
        get_raw(self);
        get_raw(val);

        # Check the new value is a integer type
        assert isinstance(val, int)

        # Check the new value is smaller than the maxval (pre-allocated memory size)
        assert val < self.maxval

        # PyVarObject->ob_size
        val_ob_size_ushort = ctypes.c_ushort.from_address(id(val)+16)
        val_ob_size = ctypes.c_short.from_address(id(val)+16)
        val_ob_digit0 = ctypes.c_uint.from_address(id(val)+24)
        val_ob_digit1 = ctypes.c_uint.from_address(id(val)+24+4)
        self_ob_size = ctypes.c_short.from_address(id(self)+16)
        self_ob_size_ushort = ctypes.c_ushort.from_address(id(self)+16)
        self_ob_digit0 = ctypes.c_uint.from_address(id(self)+24)
        self_ob_digit1 = ctypes.c_uint.from_address(id(self)+24+4)

        if val_ob_size.value == 0:
            self_ob_size.value = 0
            self_ob_digit = ctypes.c_long.from_address(id(self)+24)
            self_ob_digit.value = 0
        else:
            if val_ob_size.value < 0:
                self_ob_size_ushort.value = val_ob_size_ushort.value
            #    self_ob_size_ushort.value = 65535 
            #else:
            #    self_ob_size.value = val_ob_size.value;
            #self_ob_size.value = 1
            
            count = abs(self_ob_size.value)
            print("count:", count)

            # PyLongObject->ob_digit
            if count != 0:
                count = 2
                ctypes.memmove(id(self)+24, id(val)+24, (count*4))
            #self_ob_digit0.value = 200
            #self_ob_digit1.value = 0

        print('val ob_size ushort:', val_ob_size_ushort.value)
        print('val ob_size:', val_ob_size.value)
        print('val ob_digit[0]:', hex(val_ob_digit0.value))
        print('val ob_digit[1]:', hex(val_ob_digit1.value))
        print('self ob_size ushort:', self_ob_size_ushort.value)
        print('self ob_size:', self_ob_size.value)
        print('self ob_digit[0]:', hex(self_ob_digit0.value))
        print('self ob_digit[1]:', hex(self_ob_digit1.value))
 
class MyInt(MutableInt):
    pass


