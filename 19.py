# I/P : "AC*wv12n/:#e123we2.45oni(foi6n#98ne"
# O/P : [2.45, 6, 12, 98, 123x]

str1 = "AC*wv12n/:#e123we2..45oni(0.21foi6n#98ne"
temp = ""
data = []

for ch in str1:
    if ch.isdigit() or (ch == "." and "." not in temp):
        temp = temp + ch
    elif len(temp) != 0:
        data.append(eval(temp))
        temp = ""
    
print(sorted(data))
