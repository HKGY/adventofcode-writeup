a = input()
for i in range(len(a)):
    t = 0
    b = a[i:i + 14]
    for j in range(14):
        for k in range(14):
            if b[j] == b[k]:
                t = t+1
    if t == 14:
        print(i+14)
        break

