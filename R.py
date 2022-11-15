x = int(input())

def prostBroj(x):
    if x > 1:
        for i in range(2,x//2):
            if x%i==0:
                return False
        return True
a=1
y=x
while y>1:
    if prostBroj(y):
        a=y
        break
    else:
        y-=1
y=x
b=x
while y:
    if prostBroj(y):
        b=y
        break
    else:
        y+=1

if a==b:
    print(a)
elif abs(x-a)==abs(x-b):
    print(a,b)
elif abs(x-a)>abs(x-b):
    print(b)
else:
    print(a)
