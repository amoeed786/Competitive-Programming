def array(ar):
    count=0
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            if i<j and (ar[i] -ar[j] == i-j):
                count += 1
    return count
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr =list(map(int,input().split()))
        print(array(arr))
