def p(n):
  for i in range(2,n):
    if (n%i) == 0:
      return 0
  return 1
a=int(input())
n=list(map(int,input().split()))
k=int(input())
c=0
for i in n:
    if i>=k:
        if p(i)==1:
            c+=1
print(c)