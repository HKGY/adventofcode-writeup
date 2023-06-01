aim = x = y = 0
for i in range(1000):
    n = str.split(input())
    a = n[0]
    b = int(n[1])
    if a == "down":
        aim = aim + b
    elif a == "up":
        aim = aim - b
    elif a == "forward":
        x = x + b
        y = y + b * aim
    i = i + 1
print(x*y)

