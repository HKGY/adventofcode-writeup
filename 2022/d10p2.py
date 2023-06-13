c = 0
q = 1
draw = []
for i in range(139):
    p = input()
    if len(p.split()) == 2:
        a,b = p.split()
        c = c + 1
        if c % 40 in [q-1,q,q+1]:
            draw.append('#')
        else:
            draw.append(".")
        c = c + 1
        q = q + int(b)
        if c % 40 in [q-1,q,q+1]:
            draw.append('#')
        else:
            draw.append(".")
    else:
        c = c + 1
        if c % 40 in [q-1,q,q+1]:
            draw.append('#')
        else:
            draw.append(".")
for i in range(6):
    for j in range(40):
        print(draw[40*i+j],end='')
    print('')
    


    

