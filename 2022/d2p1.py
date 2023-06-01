sum = 0
for i in range(2500):
    a,b=input().split()
    if a == 'A' and b =='Y' or a == 'B' and b == 'Z' or a == 'C' and b =='X':
        sum = sum + 6
    if a == 'A' and b =='X' or a == 'B' and b == 'Y' or a == 'C' and b =='Z':
        sum = sum + 3
    if a == 'A' and b =='Z' or a == 'B' and b == 'X' or a == 'C' and b =='Y':
        sum = sum + 0
    if b == 'X':
        sum = sum + 1
    if b == 'Y':
        sum = sum +2
    if b == 'Z':
        sum = sum +3
print (sum)
    