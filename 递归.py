d=[1,1,2]
def dg(a):
    if a < len(d) and d[a]!=0:
        return d[a]
    else:
        d.append(dg(a-1)+ dg(a-2) )
        return d[a]
    
for i in range(100):
    print(dg(i),end=' ')

