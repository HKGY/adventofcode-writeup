sum = 0
r = [[0,0]]
x = [0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0]
for i in range(2000):
    a,b = input().split()
    b = int(b)
    if a == 'U':
        for j in range(b):
            y[0] = y[0] + 1
            for k in range(9):
                if y[k+1] < y[k] - 1 or y[k+1] > y[k] + 1 or x[k+1] < x[k] - 1 or x[k+1] > x[k] + 1:
                    if x[k+1] == x[k] - 2:
                        x[k+1] = x[k] - 1
                    elif x[k+1] == x[k] + 2:
                        x[k+1] = x[k] + 1
                    else:
                        x[k+1] = x[k]  
                    if y[k+1] == y[k] - 2:
                        y[k+1] = y[k] - 1
                    elif y[k+1] == y[k] + 2:
                        y[k+1] = y[k] + 1
                    else:
                        y[k+1] = y[k]                   
                if [x[9],y[9]] not in r:
                    r.append([x[9],y[9]])
    if a == 'R':
        for j in range(b):
            x[0] = x[0] + 1
            for k in range(9):
                if y[k+1] < y[k] - 1 or y[k+1] > y[k] + 1 or x[k+1] < x[k] - 1 or x[k+1] > x[k] + 1:
                    if x[k+1] == x[k] - 2:
                        x[k+1] = x[k] - 1
                    elif x[k+1] == x[k] + 2:
                        x[k+1] = x[k] + 1
                    else:
                        x[k+1] = x[k]  
                    if y[k+1] == y[k] - 2:
                        y[k+1] = y[k] - 1
                    elif y[k+1] == y[k] + 2:
                        y[k+1] = y[k] + 1
                    else:
                        y[k+1] = y[k]                    
                if [x[9],y[9]] not in r:
                    r.append([x[9],y[9]]) 
    if a == 'D':
        for j in range(b):
            y[0] = y[0] - 1
            for k in range(9):
                if y[k+1] < y[k] - 1 or y[k+1] > y[k] + 1 or x[k+1] < x[k] - 1 or x[k+1] > x[k] + 1:
                    if x[k+1] == x[k] - 2:
                        x[k+1] = x[k] - 1
                    elif x[k+1] == x[k] + 2:
                        x[k+1] = x[k] + 1
                    else:
                        x[k+1] = x[k]  
                    if y[k+1] == y[k] - 2:
                        y[k+1] = y[k] - 1
                    elif y[k+1] == y[k] + 2:
                        y[k+1] = y[k] + 1
                    else:
                        y[k+1] = y[k]                     
                if [x[9],y[9]] not in r:
                    r.append([x[9],y[9]]) 
    if a == 'L':
        for j in range(b):
            x[0] = x[0] - 1
            for k in range(9):
                if y[k+1] < y[k] - 1 or y[k+1] > y[k] + 1 or x[k+1] < x[k] - 1 or x[k+1] > x[k] + 1:
                    if x[k+1] == x[k] - 2:
                        x[k+1] = x[k] - 1
                    elif x[k+1] == x[k] + 2:
                        x[k+1] = x[k] + 1
                    else:
                        x[k+1] = x[k]  
                    if y[k+1] == y[k] - 2:
                        y[k+1] = y[k] - 1
                    elif y[k+1] == y[k] + 2:
                        y[k+1] = y[k] + 1
                    else:
                        y[k+1] = y[k]                    
                if [x[9],y[9]] not in r:
                    r.append([x[9],y[9]]) 
print(len(r))

