# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


nums = [-2,1,-3,4,-1,2,1,-5,4]

summ = 0
maxx = nums[0]
for i in nums:
    if summ < 0:
        summ = 0

    summ += i
    maxx = max(maxx,summ)

print(maxx)
