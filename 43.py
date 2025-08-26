# sam forgot his password of his super locker. He remembers the numbers of digits n as well as the sum of the digits is s.
# He knows that his password is the largest number of n digits that can be made with given sum s. 
# OP: 93000



n = 5
s = 12

list = [0]*n
nine = 9
l = s

for i in range(n):
    if nine<=l:
        list[i]=nine
        l -= nine
    else:
        list[i] = l
        l -= l

if sum(list) != s:
    print(-1)
else:
    ans = ''
    for i in list:
        ans += str(i)

print(ans)
