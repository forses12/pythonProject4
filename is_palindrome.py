def is_palindrome(x):
    a=0
    c=len(str(x))
    for num in range(c):
        num+=1
        b=x%10
        a+=b*(10**(c-num))
        x=x//10

    return a
print(is_palindrome(1234567890))