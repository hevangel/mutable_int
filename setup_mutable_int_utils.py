# setenv PYTHONPATH `pwd`/lib/python3.5/site-packages/
# python setup_mutable_int_utils.py install --prefix=`pwd`

from distutils.core import setup, Extension
setup(name = 'mutable_int_utils', version = '1.0',  \
   ext_modules = [Extension('mutable_int_utils', ['mutable_int_utils.c'])])
