# IP: [1,2,2,2,3,3,4,5,5,6,6,7,7,7,8,9]
# OP: [1,4] only elements which occur once

mylist = [1,2,2,2,3,3,4,5,5,6,6,7,7,7,8,9]
newlist = []
for num in mylist:
    if mylist.count(num)==1:
        newlist.append(num)

print(newlist)
