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


Output:
  2178
  
