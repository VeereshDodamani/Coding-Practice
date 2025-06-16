# An e-commerce site has a series of ads to display. Links to the ads are stored in data structure and they are displayed or not in based on the value at bit position in a number.
# the sequence of ads being displayed at this time can be represented as binary value. Where 1 means the ad is displayed and 0 means ad is not displayed. The ads should rotate.
# So, when the next page loads, ads that are displayed now are hidden and vice-versa.

def changeads(num):
    b = bin(num)
    b = b[2:len(b)]
    print(f"The {num} in binary is : {b}")
    b1=""

    for i in range(len(b)):
        if b[i]=='1':
            b1 = b1+'0'
        else:
            b1 = b1+'1'
    print(f"The negated value of {num} is : {b1}")

    sum1 = 0
    for i in range(len(b)):
        sum1 += int(b1[i])*(2**(len(b1)-(i+1)))
    print(f"The integer value of {b1} is : {sum1}")

changeads(50)
changeads(30)
changeads(25)
