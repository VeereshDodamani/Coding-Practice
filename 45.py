# If the given string contains >=4 consecutive consonants then it is hard to pronounce
# For the given string find out weather the string is hard to pronounce or not

s = input("Enter the string: ")
s = s.lower()

vowels = ['a','e','i','i','o','u']
count = 0

for i in s:
    if i not in vowels:
        count += 1
        if count == 4:
            break
    else:
        count = 0

if count >= 4:
    print("Hard")
else:
    print("Easy")
