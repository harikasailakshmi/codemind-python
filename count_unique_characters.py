n=input()
n=n.lower()
t='a'
a=list(n.strip())
o=0
for i in range(ord(t),(ord(t)+27)):
    c=0
    for j in a:
        if chr(i)==j:
            c+=1
    if c==1:
        o+=1
    t=chr(ord(t)+1)
print(o)