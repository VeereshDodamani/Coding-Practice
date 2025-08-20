# Write a function that reverses a string. The input string is given as an array of characters s.
# input, s = "mynameis"
# output, s = "siemanym"

s = "mynameis"
print("Given string: ",s)
print("Way-1")
i = len(s)-1
a = []

while i>=0:
    a.append(s[i])
    i -= 1
reversed_string = "".join(a)
print("Reversed string: ",reversed_string)


print("Way-2")
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s = list("mynameis")
print("Reversed string:", "".join(reverseString(s)))
