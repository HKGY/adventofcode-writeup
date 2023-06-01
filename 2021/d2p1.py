i = x = y = 0
for i in range(1000):
    n = str.split(input())
    a = n[0]
    b = int(n[1])
    if a == "down":
        y = y + b
    elif a == "up":
        y = y - b
    else:
        x = x + b
    i = i + 1
print(x*y)

