test=int(input())
while test:
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if i%2!=0:
            c+=1
    if c%2!=0:
        c-=1
    print(c//2)