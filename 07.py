# Write a program for finding pair of highest product

arr1 = [5,3,1,4,3,7,6,9,2]

num1 = 0
num2 = 0
tuple1 = ()

for i in range(len(arr1)):
    if arr1[i]>=num1:
        num1 = arr1[i]
tuple2 = tuple1 + (num1,)

arr1.remove(num1)

for i in range(len(arr1)):
    if arr1[i]>=num2:
        num2 = arr1[i]
arr1.remove(num2)

tuple3 = tuple2 + (num2,)
print(tuple3)
