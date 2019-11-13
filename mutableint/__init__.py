import copy
import _mutableint

class MutableIntBase():
    """
    Base class for mutlable int object
    Need to seperate the __new__ in a base class to workaround the limitation initial memory allocation of Python object
    So it won't point to the preallocated int object in range -5 to 255
    """
    enable_MutableInt = True

    def __new__(cls, val, maxval=0xFFFFFFFF):
        if cls.enable_MutableInt:
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

    use_id_for_hash = False

    def __init__(self, val, maxval=0xFFFFFFFF):
        """keep track of the maximum value supported by the pre-allocated memory size"""
        if type(self).enable_MutableInt:
            self.maxval = maxval
            self.set(val)

    def __int__(self):
        """Return a normal int object"""
        if type(self).enable_MutableInt:
            return self.val
        else:
            return self

    def __index__(self):
        """Return a normal int object"""
        return int(self)

    def __hash__(self):
        if type(self).use_id_for_hash:
            # use the memory address as the hash value
            # so it won't get confuse with hash value of int type (which is the integer number)
            return id(self)
        else:
            # use the integer value as the hash value
            return int(self)

    def __eq__(self, other):
        """Compare using the nomral int object"""
        if type(self).enable_MutableInt:
            return int(self) == other
        else:
            return super(int).__eq__(other)

    def __iter__(self):
        """make the MutableInt object iterable as well, for convenience"""
        return iter([int(self)])

    def __copy__(self):
        """need special version of copy()"""
        cls = self.__class__
        result = cls(self.val, self.maxval)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        """need special version of deepcopy()"""
        cls = self.__class__
        result = cls(self.val, self.maxval)
        result.__dict__.update(self.__dict__)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    def set(self, val):
        """Copy the raw memory value of the integer in PyObject C data structure"""

        assert type(self).enable_MutableInt, "MutableInt is disabled"

        # Check the new value is a integer type
        assert isinstance(val, int), "new value is not an int"

        # Check the new value is smaller than the maxval (pre-allocated memory size)
        assert abs(val) < self.maxval, "new value is larger than the preallocated memory size"

        self.val = val
        if val == 0:
            # zero is a special case, need to reset the ob_size
            _mutableint.copy_int(self, self.maxval)
        _mutableint.copy_int(self, val)








