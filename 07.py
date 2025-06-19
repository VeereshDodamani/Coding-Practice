# Write a program for finding pair of highest product

arr1 = eval(input("Enter the array : "))
def find_max_product(arr1):
    if len(arr1)<2:
        print("Elements less than 2")

    a = arr1[0]
    b = arr1[1]

    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i]*arr1[j] > (a*b):
                a = arr1[i]
                b = arr1[j]
    return (a,b)

print(find_max_product(arr1))
