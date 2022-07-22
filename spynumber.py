#sum of digits must be equal to the product of digits of the number
def isSpy(num):
    s=0
    m=1
    while num:
        rem=num%10
        num=num//10
        s+=rem
        m*=rem
    return m==s

num=int(input())
res=isSpy(num)
print(res)



Output:
  1124
True
