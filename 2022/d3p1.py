sum = 0
for i in range(300):
    a = input()
    b = len(a)
    c = a[:b//2]
    d = a[b//2:]
    e = []
    for j in range(b//2):
        for k in range(b//2):
            if c[j] == d[k] and c[j] not in e:
                e.append(c[j])
                if c[j].isupper():
                    sum = sum + ord(c[j]) - 38
                else:
                    sum = sum + ord(c[j]) - 96
print(sum)



