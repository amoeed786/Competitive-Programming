def stripes(n,k,strip):
    colur=0
    total=0
    for i in range(n):
        if strip[i]=='B':
            colur +=1
        else:
            total=max(total,colur)
            colur=0
    return max(0,k-total)

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    strip=input()
print(stripes(n,k,strip))
