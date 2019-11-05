import ctypes
try:
    import mutable_int_utils
except:
    print("Warning: Unable to Import mutable_int_utils, please run setup_mutable_int_utils.py")

enable_MutableInt = True

class MutableIntBase():
    """
    Base class for mutlable int object
    Need to seperate the __new__ in a base class to workaround the limitation initial memory allocation of Python object
    So it won't point to the preallocated int object in range -5 to 255
    """
    def __new__(cls, val, maxval=0xFFFFFFFF):
        if enable_MutableInt:
            return int.__new__(cls, maxval)
        else:
            return int.__new__(cls, val)

class MutableInt(MutableIntBase, int):
    """
    Mutable int object
    Python int type is immutable (i.e., its value can't be chagne once the object is created)
    Python allocate memory required for the int object for each integer value exactly once per number.
    Integer from -5 to 255 is already preallocated and all new instances merely point to the exsiting int objects

    Python int is stored in the following formart in the memory
    PyObject->ob_size (2 bytes) - stores the number of the digits in the integer.
        ob_size = 0 means int is zero
        ob_size < 0 means the int is a negative number
    PyObject->ob_digit[n] (n bytes) - stores the digits of the integer number.
        each digit only has 30 bits.
        so for example a 32 bits integer has 2 digits

    Since the memory of the int object is allocated when the object is created,
    we need to pre-allocate enough ob_digit[n] to support the maximum value (the maxval argument)

    For some reason, I can't set the mutable integer value to negative number.
    It should work but Python segfault everytime it try to do arithmic operation on a negative number
    Just make it illegal to assign negative value for now, we don't need negative value in G5SW
    """

    def __init__(self, val, maxval=0xFFFFFFFF):
        # keep track of the maximum value supported by the pre-allocated memory size
        if enable_MutableInt:
            self.maxval = maxval
            self.set(val)

    def __int__(self):
        # Return a normal int object
        if enable_MutableInt:
            return self.val
        else:
            return self

    def __index__(self):
        # Return a normal int object
        return int(self)

    def __hash__(self):
        # use the memory address as the hash value
        # so it won't get confuse with hash value of int type (which is the integer number)
        return int(self)

    def __eq__(self, other):
        # Compare using the nomral int object
        if enable_MutableInt:
            return int(self) == other
        else:
            return super(int).__eq__(other)

    def __iter__(self):
        # make the MutableInt object iterable as well, for convinience
        return iter([int(self)])

    def set(self, val):
        assert enable_MutableInt, "MutableInt is disabled"
        # Copy the raw memory value of the integer in PyObject C data structure

        # Check the new value is a integer type
        assert isinstance(val, int), "new value is not an int"

        # Check the new value is smaller than the maxval (pre-allocated memory size)
        assert val >= 0, "MutableInt does not support negative number"
        assert val < self.maxval, "new value is larger than the preallocated memory size"

        self.val = val
        mutable_int_utils.copy_int(self, val)








