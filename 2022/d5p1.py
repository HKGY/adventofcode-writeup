a=[]
for i in range(9):
    a.append([])
for i in range(8):
    x = input()
    for j in range(9):
        if x[1 + 4 * j] != ' ':
            a[j].append(x[1 + 4 * j])
input()
input()
for i in range(501):
    y = input().split()
    m = int(y[1])
    f = int(y[3])-1
    t = int(y[5])-1
    for j in range(m):
        a[t].insert(0,a[f].pop(0))
for i in range(9):
    print(a[i][0], end='')