# Find 2nd larget element in list

# Way-1: Sort and print 2nd largest number
lis = [23,12,45,43,67,64]
lis.sort()
print("Way-1")
print(f"Second largest number: {lis[-2]}")

# Way-2: Remove largest number and print max
lis.pop()
print("Way-2")
print(f"Second largest number: {lis[-1]}")

# Way-3: Manual method
largest = lis[0]
sec_largest = lis[0]
for i in range(len(lis)):
    if lis[i]>=largest:
        largest = lis[i]


for i in range(len(lis)):
    if lis[i] > sec_largest and lis[i]!=largest:
        sec_largest = lis[i]

print("Way-3")
print(f"Largest number: {largest}")
print(f"Second largest number: {sec_largest}")
