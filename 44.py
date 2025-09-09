# Given a string. Reverse each word in it where the words are seprated by dots.

s = "i.like.this.program.very.much"
print("Acual String: ",s)

def reverse(s):
    l = list(s.split("."))
    k = []

    for i in l:
        rev = i[::-1]
        k.append(rev)

    return ".".join(k)

print("Reversed string: ",reverse(s))
