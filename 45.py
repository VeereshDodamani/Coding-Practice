s = input()
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
