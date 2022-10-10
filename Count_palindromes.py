n=int(input())
b=list(map(int,input().split()))
a=[]
for i in b:
    a.append(abs(i))
a=map(str,a)
c=0
for i in a:
    if i==i[::-1]:
        c+=1
print(c)