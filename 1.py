def convert(n):
    if n<3:
        return str(n)
    s = ''
    while n != 0:
        s = str(n%3) + s
        n=n//3
    return s
        
a=int(input())
print(convert(a))