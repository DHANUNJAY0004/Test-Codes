
def count(s,c):
    x=0
    for i in s:
        if i == c:
            x=x+1
    return x
str1=input()
str2=input()
print(count(str1,str2[-1]))