t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    b=[]
    i=j=4*n-2
    for i in range(4*n-1):
        x,y=input().split()
        a.append(int(x))
        b.append(int(y))
        
    while i>=0:
        s=a[i]
        a.remove(s)
        if s not in a:
            mx=s
            i=-1
        else:
            a.append(s)
            i=-1
    while j>=0:
        m=b[j]
        b.remove(m)
        if m not in b:
            my=m
            j=-1
        else:
            b.append(m)
            j=-1
    print(mx,my)