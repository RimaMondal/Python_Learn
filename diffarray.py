from numpy import *
arr = array([1,2,3,4,5])
print(arr.dtype)
arr1= array([1,2,3,4],float)
print(arr1)

arr2= linspace(0,15,16)
print(arr2)

arr3=arange(1,15,2)
print(arr3)

arr4=logspace(1,40,5)
print(arr4)
print('%.2f' %arr4[0])


arr5=zeros(5,int)
print(arr5)

arr6=ones(3)
print(arr6)



arr = array([1,2,3,4,5])
arr = arr+5
print(arr)


#add two arrays
arr1=array([1,2,3,4,5])
arr2=array([6,1,9,3,2])
arr3=arr1+arr2
print(arr3)
print(concatenate([arr1,arr2]))


arr4=array([2,3,4])
arr4[1]=9
#arr5=arr4.view()
arr6=arr4.copy()
print(arr4)
print(arr5)
print(id(arr4))
#print(id(arr5))
print(id(arr6))











