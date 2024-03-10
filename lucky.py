def lucky(n):
    luckynumbers=[4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    if 1<=n<=1000:
        for lucky in luckynumbers:
            if n%lucky==0:
                return ("YES")
        for i in str(n):
            if i not in ['4','7']:
                return "NO"
        return "YES"
n=int(input())
print(lucky(n))