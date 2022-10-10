def p(a):
    if a<2:
        return 0
    else:
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in a:
    if p(i)==1:
        k+=1
        c+=i
print("%.2f"%(c/k))