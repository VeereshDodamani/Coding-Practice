# Write the code for following requirements
# If input 2 512
# 2*2 = 4*2 = 8*2 ........ = 512
# Output
# Count = 8


value = int(input("Enter the value : "))
count = 0
x=2
while (x!=value):
    x = x*2
    count += 1
print(count)
