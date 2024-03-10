def palindrome(x):
    if -2147483648<=x<=2147483647:
        string=str(x)
        reversestr=string[::-1]
        if string == reversestr:
            return True
        else:
            return False
    return False
x=-121
print(palindrome(x))