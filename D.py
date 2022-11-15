niska = input()
x=""
i=0
niz=[]
for i in range(len(niska)):
    if i!=len(niska)-1 and niska[i]==niska[i+1]:
        x+=niska[i]
    else:
        if len(x)>0:
            x+=niska[i]
            niz.append(x)
            x=""
for i in niz:
    niska = niska.replace(i,i[0]+str(len(i)))
print(niska)
