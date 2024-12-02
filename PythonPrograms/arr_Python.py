#import array as arr
from array import *

val = array('i', [4,7,-8,5,88, 44])
print(val)
print(val.buffer_info())
#val.reverse()
print(val)
#Creae\te a New Array from existing one #
newArr = array(val.typecode, (x*x for x in val))
print(newArr)
for _ in newArr:
    print(_)
#Print ARRAY in python #
arr = [2,4,5,7,9]
print("The Array is :", arr)    