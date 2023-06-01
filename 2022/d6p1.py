a = input()
for i in range(len(a)):
    b = a[i:i + 4]
    if not (b[0] == b[1] or b[0] == b[2] or b[0] == b[3] or b[1] == b[2] or b[1] == b[3] or b[2] == b[3]):
        print(i+4)
        break

