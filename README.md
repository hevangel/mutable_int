# Python Mutable Integer package, a subclass of int

## Install
> 'pip install mutableint'

This package is a proof of concept implemenation of a mutable integer object for Python.
The mutable integer class is a sub-class of the built-in int class.   
The mutable integer object feels like an int, works like an int, it even works exactly like an int when the Python object is passed into C code via SWIG

## Usage
```python
from mutableint import MutableInt

# create a mutable integer with value 10 
a = MutableInt(10)

# change the value of a to 11
a.set(11)
```

## Development

Install and compile the package locally

> 'python setup install'

Run the unit tests

> 'python test_mutableint.py
