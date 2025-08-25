# Given a singly linked list, the task is to check if the given linked list is palindrome or not.

print("Way-1")
nums = [1, 2, 3, 2, 1]
n = len(nums)

is_palindrome = True
for i in range(n // 2):
    if nums[i] != nums[n - 1 - i]:
        is_palindrome = False
        break

print("Given array is: ",is_palindrome)

print("Way-2")
nums = [1, 2, 3, 4, 5, 3, 2, 1]
l, r = 0, len(nums)-1

palindrome = True
while l<=r:
    if nums[l]!=nums[r]:
        palindrome = False
        break
    else:
        l+=1
        r-=1

print("Given array is: ",palindrome)
