a=int(input())
n=list(map(int,input().split()))
for i in range(a):
    print(len(str(abs(n[i]))),end=" ")