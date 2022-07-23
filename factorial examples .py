'''
def fun(n):
    if n<=0:
        return
    fun(n-1)
    print(n)
    fun(n-2)
n=int(input())##5
fun(n)
'''###1 2 3 1 4 1 2 5 1 2 3 1

'''
def fun(n):
    if n<=0:
        return n
    return fun(n-1)+fun(n-2)
n=int(input())##5
res=fun(n)
print(res)
'''### -5

'''
def fun(n):
    if n<=0:
        return n
    return n+fun(n-1)+fun(n-2)
n=int(input())#5
res=fun(n)
print(res)
'''## 21

'''
def fun(n):
    if n==0:
        return 
    print(n)
    fun(n-1)
n=int(input())##5
fun(n)
''' 5 4 3 2 1

'''
def fun(n):
    if n==0:
        return 
    fun(n-1)
    print(n)
n=int(input())## 5
fun(n)
'''## 1 2 3 4 5
