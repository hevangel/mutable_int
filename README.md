# Python Mutable Integer package, a subclass of int

## Install
> 'pip install mutableint'

This package is a proof of concept implemenation of a mutable integer object for Python.  The mutable integer class is a sub-class of the built-in int class.   

The mutable integer object feels like an int, works like an int, it even works exactly like an int when the Python object is passed into C code via SWIG

## Usage
```python
from mutableint import MutableInt

# create a mutable integer with value 10 
foo = MutableInt(10)

# check type
isinstance(foo,int)
>True

# copy the variable
bar = foo

# change the value of foo to 11
foo.set(11)

# check both variables are updated
print(foo, bar)
>11 11
```

## Implementation Details
Python int type is immutable (i.e., its value can't be chagne once the object is created)

Python allocate memory required for the int object for each integer value exactly once per number.
Integer from -5 to 255 is already preallocated and all new instances merely point to the exsiting int objects

Python int is stored in the following format in the memory
- PyObject->ob_size (2 bytes) - stores the number of the digits in the integer.
  - ob_size = 0 means int is zero
  - ob_size < 0 means the int is a negative number
- PyObject->ob_digit[n] (n bytes) - stores the digits of the integer number.
  - each digit only has 30 bits.
  - so for example a 32 bits integer has 2 digits

Since the memory of the int object is allocated when the object is created,
we need to pre-allocate enough ob_digit[n] to support the maximum value (the maxval argument)

A C function is created to update the memory content of ob_size and ob_digit[]  

## Development

Install and compile the package locally

> 'python setup.py install'

Run the unit tests

> 'python test_mutableint.py
