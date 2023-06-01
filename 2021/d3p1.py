num=c=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    x=input()
    for j in range(12):
        if(x[j]=='0'):
            c[j]=c[j]-1
        elif(x[j]=='1'):
            c[j]=c[j]+1
for i in range(12):
    if(c[i]>0):
        num[i]=1
    elif(c[i]<0):
        num[i]=0
gamma = num[0]*2048+num[1]*1024+num[2]*512+num[3]*256+num[4]*128+num[5]*64+num[6]*32+num[7]*16+num[8]*8+num[9]*4+num[10]*2+num[11]
for i in range(12):
    if(num[i]==0):
        num[i]=1
    elif(num[i]==1):
        num[i]=0
epsilon = num[0]*2048+num[1]*1024+num[2]*512+num[3]*256+num[4]*128+num[5]*64+num[6]*32+num[7]*16+num[8]*8+num[9]*4+num[10]*2+num[11]
print(gamma*epsilon)