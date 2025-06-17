# Write a python pgm to sort characters and numbers so that first alphabets and then numbers are printed.

str1 = input("Enter a string for sorting: ")
alphabet = []
numbers = []

for ch in str1:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        numbers.append(ch)

final_list = sorted(alphabet) + sorted(numbers)
output = ''.join(final_list)
print(output)
