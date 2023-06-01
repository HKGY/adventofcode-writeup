sum = 0
for i in range(100):
    a = input()
    b = input()
    c = input()
    e = []
    for j in range(len(a)):
        for k in range(len(b)):
            for l in range(len(c)):
                if a[j] == b[k] == c[l] and a[j] not in e:
                    e.append(a[j])
                    if a[j].isupper():
                        sum = sum + ord(a[j]) - 38
                    else:
                        sum = sum + ord(a[j]) - 96
print(sum)



