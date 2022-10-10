n=int(input())
a=list(map(int,input().split()))
if (sum(a)//n) in a:
    print("True")
else:
    print("False")