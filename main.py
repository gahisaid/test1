t=[2,15,3,14,5,1,8,11,4,9]
j= 0
tmp = 0
stable = 1
while (stable==1) :
    stable = 0
    for j in range(0,9):
        if(t[j] < t[j+1]):
            tmp = t[j+1]
            t[j+1] = t[j]
            t[j] = tmp
            stable = 1


for x in range(10):
    print(t[x])
   

