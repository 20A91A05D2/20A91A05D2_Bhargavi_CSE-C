'''
a  b
33  66 ## a is odd
16  132 
8   264
4   528
2   1056
1   2112## a is odd
result=66+2112
'''

Program:
  Without Using recursion:
  def fun(a,b):
    res=0
    while a>=1:
        if a%2!=0:
            res+=b
        a=a//2
        b=b*2
    return res


a,b=map(int,input().split())
res=fun(a,b)
print(res)

Using Recursion:
  def fun(a,b):
    if a==1:
        return b
    if a%2!=0:
        return b+fun(a//2,b*2)
    else:
        return fun(a//2,b*2)
a,b=map(int,input().split())
print(fun(a,b))


Output:
  2178
  
