# Write a function that reverses a string. The input string is given as an array of characters s.
# input, s = "mynameis"
# output, s = "siemanym"


print("Way-1")
s = "mynameis"
print("Given string: ",s)
i = len(s)-1
a = []

while i>=0:
    a.append(s[i])
    i -= 1
reversed_string = "".join(a)
print("Reversed string",reversed_string)
