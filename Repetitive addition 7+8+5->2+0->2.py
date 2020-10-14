
a=int(input());

def loop1(a):
    s=0
    while(a>0):
        rem=a%10
        s=s+rem
        a=a/10
        s=int(s)
    return s
    
while(a>=9):
    a=loop1(a)

print(a)
