# Find the Duplicate Number

nums = [3,1,3,4,2]

n1 = []

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]==nums[j]:
            n1.append(nums[i])

print(n1)
