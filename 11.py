# Given an unsorted array on size n. Array elements are in the range of 1 to n. 1 number is missing from the set and 1 is occuring twice. Find the repeating and missing number.

arr = [4,3,6,2,1,1]
arr1 = [4,3,6,2,1,1]

for i in range(1, len(arr)):
    if i not in arr:
        print(f"Missing number : {i}")
    
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]==arr[j]:
            print(f"Repeated number : {arr[i]}")
