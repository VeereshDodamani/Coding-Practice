# Reverse Pairs

# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].

nums = [1,3,2,3,1]
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > 2 * nums[j]:
            count += 1
print(count)
