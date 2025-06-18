# Two sum problem

nums = [2,6,5,8,11]
target = 14
arr1 = []
for i in range(len(nums)):
    if target-nums[i] in nums:
        arr1.append(i)
print(arr1)
