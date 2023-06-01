sum =0
for i in range(1000):
    a, b = input().split(',')
    a1,a2 = map(int, a.split('-'))
    b1,b2 = map(int, b.split('-'))
    if not (a1 < b1 and a2 < b1 or a1 > b2 and a2 > b2):
        sum = sum + 1
print(sum)