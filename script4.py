#from array import *
#vals = array('i', [1, 2, 3, 4,5])
#print(vals)
from array import *
vals = array('i', [9, 5, 10, -1, -2])
print(vals.buffer_info())
vals.reverse()
print(vals)
print(vals[0])
from array import *
vals = array('i', [1, 2, 3, 4,5])
newarr = array('i', (a for a in vals))
for i in newarr:
    print(i)
from array import *
arr = array('i', [])
n = int(input("Enter length of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
print(arr)