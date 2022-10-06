n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in a:
    if i%2==0:
        s+=i
    else:
        s1+=i
print(abs(s-s1))
