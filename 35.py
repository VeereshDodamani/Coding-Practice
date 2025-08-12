# Write a python program for the following requirement
# IP: 'my25name45is'
# OP: 'si25eman45ym'
# Reverse the Alphabet and Integers be on same position

str1 = 'my25name45is'
print("Given string: ",str1)
output = ''

alphas = [char for char in reversed(str1) if char.isalpha()]
print("Reversed alphabets of strings: ",alphas)

i=0
for char in str1:
    if char.isalpha():
        output += alphas[i]
        i += 1
    else:
        output += char

print("Reversed given string: ",output)
