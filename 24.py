# Chech if the given string s in present in t or not.
s = "abc"
t = "ahbgdc"
def isSubsequence():
    j = 0
    for i in s:
        if i in t:
            j += 1
        else:
            pass

    if j == len(s):
        return("True")
    
print(isSubsequence())
