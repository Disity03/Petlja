t ,x = input(), input()
s=0
for i in range(len(x)-1):
    s+= abs(t.index(x[i])-t.index(x[i+1]))
print(s)
