# Find 2nd larget element in list

# Way-1: Sort and print 2nd largest number
lis = [23,12,45,43,67,64]
lis.sort()
print(f"Second largest number: {lis[-2]}")

# Way-2: Remove largest number and print max
lis.pop()
print(f"Second largest number: {lis[-1]}")
