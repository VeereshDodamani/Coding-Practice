# Given a array of numbers. Find the contiguous subarray which has the maximum sum and returns its sum


nums = [1, 2, 3, -2, 5]

max_so_far = nums[0]
max_ending = nums[0]

for i in range(1, len(nums)):
    max_ending = max(nums[i], max_ending + nums[i])
    max_so_far = max(max_so_far, max_ending)

print(max_so_far)
