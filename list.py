names=['rima','raima','tota']
nums=[10,20,30,40]
print(names)  #['rima', 'raima', 'tota']
mil=[names,nums]
print(mil)  #[['rima', 'raima', 'tota'], [10, 20, 30, 40]]
nums.append(50)
print(nums)  #[10, 20, 30, 40, 50]
nums.insert(2,77)
print(nums) #[10, 20, 77, 30, 40, 50]
nums.remove(10)
print(nums) #[20, 77, 30, 40, 50]
nums.pop(1)
print(nums) #[20, 30, 40, 50]
nums.pop()
print(nums) #[20, 30, 40]
del nums[1:]
print(nums)  #[20] // deleted from index 1 to end value
nums.extend([60,70,90,100])
print(nums) #[20, 60, 70, 90, 100]
print(min(nums)) #20
print(max(nums)) #100
print(sum(nums)) #340
nums.sort()
print(nums) #[20, 60, 70, 90, 100]



