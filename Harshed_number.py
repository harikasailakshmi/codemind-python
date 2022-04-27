number=int(input())
sum=0
rem=0

temp=number
while temp>0:
    rem=temp%10
    sum=sum+rem
    temp=temp//10
    
if number%sum==0:
    print('True')
else:
    print('False')