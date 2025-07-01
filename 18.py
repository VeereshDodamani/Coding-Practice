str1 = 'a=2&b=23&name=prakash'
print(str1.split("&"))

myList = []
for ele in str1.split("&"):
    myList.append(ele.split("="))

print(myList)
