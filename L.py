#38 poena na Petlji
a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    b.append(1)
    for j in range(len(a)):
        if i != j:
            b[i]*=a[j]
        
s= ""
for i in b:
    s+= str(i)+" "
print(s)
