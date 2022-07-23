def isHappy(num):
    if num<=9:
        return num==1 or num==7
    s=0
    while num:
        rem=num%10
        num=num//10
        s+=rem*rem
    return isHappy(s)

n=int(input())
res=isHappy(n)
print(res)



Output:
  >>203
  True
