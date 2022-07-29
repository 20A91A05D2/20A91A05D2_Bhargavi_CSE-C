def gcd(a,b):
    while b>0:
        if a<b:
            b=b%a
        else:
            a,b=b,a
    return a
n=int(input())
data=list(map(int,input().split()))
res=data[0]
for i in range(1,n):
    res=(res*data[i])//gcd(res,data[i])
print(res)
