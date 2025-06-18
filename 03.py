# Write a program to display the words that are repeted more than or equal to n times in the text

str1 = input("Enter a string : ")
n = int(input("Enter the count : "))

str1 = str1.split()
print(str1)

count = dict()

for word in str1:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

word_list = []
for key in count:
    if count[key] >= n:
        word_list.append(key)

print(word_list)
