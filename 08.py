# You are given N sticks each of negligible thickness and the ith stick has thickness A[i]
# You have to form a rectangle choosing 4 sticks

# Find the max area of rectangle that is possible
#example
# I = 5,[1,8,1,8,8]
# O = 8

def rectangle(n_sticks, arr):
    arr1 = []
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                arr1.append(arr[i])

    a = arr1[0]
    b = arr1[1]
    for i in range(0,len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i]*arr[j] > (a*b):
                a = arr1[i]
                b = arr1[j]
    return(a,b)

print(rectangle(8,[2,2,5,3,4,5,1]))
