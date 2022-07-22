import math as M
def isPerfect(num):
    res=1
    sq=int(M.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            res+=i
            res+=num//i
    return res==num

t=int(input("Enter no.of numbers:"))
for _ in range(t):
    num=int(input())
    res=isPerfect(num)
    print(res)
    
    
  Output:
    Enter no.of numbers:3
28
True
36
False
100
False
