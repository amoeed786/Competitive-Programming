def water(t):
    count =0
    result=0
    for s in range(t):
        n=int(input())
        st=input()
        for s in range(n):
            if st[s] == '.':
                count+=1
                result+=1
            if st[s]=='.' and s+2<n and st[s+1] =='.' and st[s+2]=='.':
                count+=1
                result+=2
            if result>=n:
                return count
def main():
    t=int(input())
    print(water(t))
main()