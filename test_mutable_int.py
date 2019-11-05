import faulthandler
from mutable_int import *
import pprint

faulthandler.enable()

y = MutableInt(0)
y.set(1)
y.set(6)
y.set(0)

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

print('---')
a = MutableInt(0)
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
print('---')
mutable_int_utils.copy_int(a,6)
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
print('---')
mutable_int_utils.copy_int(a,100000)
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
print('---')
mutable_int_utils.copy_int(a,-1)
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
print('---')
mutable_int_utils.copy_int(a,-200)
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
print('---')
a = 0
mutable_int_utils.print_int_info(a)
get_raw(a, 'a')
b = MutableInt(0)
mutable_int_utils.print_int_info(b)
get_raw(b, 'b')
mutable_int_utils.copy_int(b,a)

print(b+5)
print(5+b)

mutable_int_utils.print_int_info(b)
get_raw(b, 'b')
mutable_int_utils.copy_int(b,-0x87654321)
mutable_int_utils.print_int_info(b)
get_raw(b, 'b')
b.set(0x98765432)
mutable_int_utils.print_int_info(b)
get_raw(b, 'b')

print(b+5)
print(5+b)

print('---')
c = MutableInt(-10)
#mutable_int_utils.print_int_info(c)
mutable_int_utils.copy_int(c,-10)
mutable_int_utils.print_int_info(c)
get_raw(c, 'c')
mutable_int_utils.copy_int(c,0)
mutable_int_utils.print_int_info(c)
get_raw(c, 'c')
mutable_int_utils.copy_int(c,1)
print(c+5)
print(5+c)

x1 = MutableInt(0)
x2 = MutableInt(0)
x3 = MutableInt(0)
x4 = MutableInt(0)
x5 = MutableInt(0)
x6 = MutableInt(0)

