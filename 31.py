## Write the python program for the following requirement
# Find student having 2nd largest marks

my_list = [['jay',80],['viru',85],['basanthi',95],['thakur',80],['sambha',30]]

my_dict = dict(my_list)
marks = set(dict(my_list).values())
marks = sorted(marks)
print(marks[-2])

sec_largest = marks[-2]

for ele in my_list:
    if ele[1] == sec_largest:
        print("Student with 2nd largest marks:",ele[0])
