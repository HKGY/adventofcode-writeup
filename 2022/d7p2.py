sum = 10000000000000000000000000000000000
s = 0
u = 0
a = []
for i in range(1032):
    a.append(input())
    if a[i].split()[1] == "cd":
        s = s + 1
    if a[i] == "$ cd ..":
        s = s - 2
for i in range(s):
    a.append("$ cd ..")

for i in range(1032 + s):
    v = a[i].split()[0]
    if v.isnumeric():
        u = u + int(v)
r = 70000000 - u
n = 30000000 - r
for i in range(1032 + s):
    if a[i] == "$ cd ..":
        j = i
        s = 0
        while(a[j-1].split()[1] != "cd"):
            j = j-1
            v = a[j].split()[0]
            if v.isnumeric():
                s = s + int(v)
        a[i] = 'a b'
        a[j-1] = 'a b'
        if (s >= n ):
            if s - n < sum:
                sum = s - n
print(sum)
print(n + sum)


