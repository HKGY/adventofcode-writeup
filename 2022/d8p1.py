l = 99
sum = 0
a = []
for i in range(l):
    a.append(input())
for i in range(l):
    for j in range(l):
        b = 0
        b1 = b2 = b3 = b4 = 1
        for k in range(i):
            if a[i][j] <= a[k][j]:
                b1 = 0
                break
        for k in range(j):
            if a[i][j] <= a[i][k]:
                b2 = 0
                break
        for k in range(i+1,l):
            if a[i][j] <= a[k][j]:
                b3 = 0
                break
        for k in range(j+1,l):
            if a[i][j] <= a[i][k]:
                b4 = 0
                break
        if i == 0 or i == l - 1 or j == 0 or j == l - 1 or b1 + b2 + b3 + b4 > 0:
            b = 1
        sum = sum + b
print(sum)