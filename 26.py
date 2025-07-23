# Given a array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j] == target:
            print(f"Yes sum of {target} present.")
            print("Indexes are: ",i,j)
            break
        else:
            print("NO")
            break
