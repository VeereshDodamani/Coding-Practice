# "a3b4c2" -> aaabbbbcc

str1 = "a3b2c4"
output = ""
for char in str1:
    if char.isalpha():
        var = char
    else:
        num = int(char)
        output += var * num

print(output)
