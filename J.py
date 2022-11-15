def kvCif(x):
    s=0
    while x>0:
        s+=(x%10)**2
        x//=10
    return s

x = int(input())
i=0
p=False
while i < 10**3:
    if kvCif(x)==1:
        p=True
        break
    else:
        x=kvCif(x)
        i+=1
if p:
    print("da")
else:
    print("ne")
