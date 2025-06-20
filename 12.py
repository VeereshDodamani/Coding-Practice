# Iterate on list withour using loop from start to end

list1 = eval(input("Enter the list : "))
start = eval(input("Enter start index : "))
# Don't include end
end = eval(input("Enter end index : "))

def iterate(list1,start,end):
    if start < 0 or start>=end:
        return
    print(list1[start])
    iterate(list1,start+1,end)

iterate(list1,start,end)
