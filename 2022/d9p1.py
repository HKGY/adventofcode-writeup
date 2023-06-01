sum = 0
r = [[0,0]]
x1 = y1 = x2 = y2 = 0
for i in range(2000):
    a,b = input().split()
    b = int(b)
    if a == 'U':
        for j in range(b):
            y1 = y1 + 1
            if y1 < y2 - 1 or y1 > y2 + 1:
                y2 = y2 + 1
                x2 = x1
                if [x2,y2] not in r:
                    r.append([x2,y2]) 
    if a == 'R':
        for j in range(b):
            x1 = x1 + 1
            if x1 < x2 - 1 or x1 > x2 + 1:
                x2 = x2 + 1
                y2 = y1
                if [x2,y2] not in r:
                    r.append([x2,y2]) 
    if a == 'D':
        for j in range(b):
            y1 = y1 - 1
            if y1 < y2 - 1 or y1 > y2 + 1:
                y2 = y2 - 1
                x2 = x1
                if [x2,y2] not in r:
                    r.append([x2,y2]) 
    if a == 'L':
        for j in range(b):
            x1 = x1 - 1
            if x1 < x2 - 1 or x1 > x2 + 1:
                x2 = x2 - 1
                y2 = y1
                if [x2,y2] not in r:
                    r.append([x2,y2]) 
print(len(r))
