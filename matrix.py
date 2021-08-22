from numpy import *


arr1= array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(arr1)
print(arr1.dtype) #int64
print(arr1.ndim) #2
print(arr1.shape) #(2,3)
print(arr1.size) #6

arr2 = arr1.flatten()
print(arr2) #[1 2 3 4 5 6]

arr3=([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

#arr4= arr
#arr4=arr3.reshape(2,2,3)
#print(arr4)


m=matrix('1,2,3,6;4,5,6,7')
print(m)
m1=matrix('1,7,0,4;5,6,7,8')
print(m1)

m3=m1+m

print('sum of matrix is',m3)
print(diagonal(m1))
m4=m*m1
print('multiplication is',m4) #error




