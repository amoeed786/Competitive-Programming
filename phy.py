t=int(input())
num=[]
vector=[]
sum_1=0
sum_2=0
sum_3=0
if 1<=t<=100:
    for i in range(t):
        n,m,a=map(int,input().split())
        num.append((n,m,a))
for i in num:
    sum_1 += i[0]
    sum_2 += i[1]
    sum_3 += i[2]
if sum_1==0 and  sum_2==0 and sum_3 == 0:
    print("YES")
else:
    print("NO")
