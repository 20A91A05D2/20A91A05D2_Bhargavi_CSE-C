'''
a    b
24   36
24   36%24=12    ##a<b---->b=b%a
24   12          ##a>b----->swap a,b
12   24
12   24%12=0     ##b=0 then gcd is a
'''


def gcd(a,b):
    while b>0:
        if a<b:
            b=b%a
        else:
            a,b=b,a
    return a

a,b=map(int,input().split())
res=gcd(a,b)
lcm=(a*b)//res
print(lcm)
