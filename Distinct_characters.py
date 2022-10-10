n=input()
n=n.lower()
t='a'
a=list(n.strip())
for i in range(ord(t),(ord(t)+27)):
    c=0
    for j in a:
        if chr(i)==j:
            c+=1
    if c==1:
        print(chr(i),end="")
    t=chr(ord(t)+1)