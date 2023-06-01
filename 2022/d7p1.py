sum = 0
a = []
for i in range(1032):
    a.append(input())
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
        if (s <=100000 ):
            sum = sum +s
print(sum)


