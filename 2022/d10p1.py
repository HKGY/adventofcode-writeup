sum = c = 0
q = 1
for i in range(139):
    p = input()
    if len(p.split()) == 2:
        a,b = p.split()
        c = c + 1
        if c in [20,60,100,140,180,220]:
            sum = sum + c * q
        c = c + 1
        if c in [20,60,100,140,180,220]:
            sum = sum + c * q
        q = q + int(b)     
    else:
        c = c + 1
        if c in [20,60,100,140,180,220]:
            sum = sum + c * q
print(sum)


    

