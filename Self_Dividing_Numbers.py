a=int(input())
b=int(input())
for i in range(a,b+1):
    g=str(i)
    c=list(map(int,g.strip("")))
    for j in c:
        if j != 0 :
            if i%j==0:
                c=1
            else:
                c=0
                break
        else:
            c=0
            break
    if c==1:
        print(i,end=" ")