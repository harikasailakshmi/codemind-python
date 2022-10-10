n=int(input())
a=list(map(int,input().split()))
print(abs(abs(sum(a[:(n//2)]))-abs(sum(a[(n//2):]))))