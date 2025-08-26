# Check if the given string is plaindrome or not.
# Ignore all the white spaces, special characters and etc.

s = "I am :IronnorI Ma, i"

word = []
for i in s:
    if i.isalpha():
        word.append(i.lower())

print(word)

palindrome = True
for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1]:
        palindrome = False
        break

print("Given string is Palindrome: ",palindrome)
