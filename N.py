x= int(input())
s=0
while x>0:
    if (x%10)%2==1:
        s+=x%10
    x//=10
print(s)
