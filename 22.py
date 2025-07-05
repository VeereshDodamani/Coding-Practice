# IP: ['1234python2666','654java763','43hadoop392']
# OP: 
# int = [12342666, 654763, 43392]
# str = [python, java, hadoop]

p = ['1234python2666','654java763','43hadoop392']
list1 = []
list2 = []
for i in p:
    int_v = ""
    char_v = ""
    for j in i:
        if j.isdigit():
            int_v += j
        else:
            char_v += j
    list1.append(int_v)
    list2.append(char_v)

print(list1)
print(list2)
