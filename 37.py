# Write a python program to move all the even number to the front while maintaing the order of the numbers.
# Odd numbers should also follow their original order

nums = [1,2,3,4,5,6,7,8,9,10]
s= []
for num in nums:
    if num%2 == 0:
        s.append(num)

for num in nums:
    if num not in s:
        s.append(num)
print(s)
