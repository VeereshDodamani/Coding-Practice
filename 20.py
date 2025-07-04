# IP: "SKY IS BLUE"
# OP: "BLUE IS SKY"

str1 = "sky is blue"
mylist = str1.split()
mylist = mylist[::-1]
print(mylist)
str2 = " ".join(mylist)
print(str2)
