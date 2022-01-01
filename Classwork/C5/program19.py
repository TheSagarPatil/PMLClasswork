import array as PY_ARRAY
import numpy as NP
py_array = PY_ARRAY.array('i', [1,2,3])
print(type(py_array))
py_array2 = PY_ARRAY.array('u', ["a","b"])
print(type(py_array))


array2 = NP.array([1,2,3,4,5])
array3 = NP.array(['sagar','type22','q'])

print(type(array2))
print(type(array3))
print(array3.dtype)

for item in array3:
    print(item)
index = 0
while index != len(array3):
    print(array3[index])
    index+=1


