import math as M
i=1
n=int(input())
sq=int(M.sqrt(n))
def factors_sum(n):
    global i
    v=0
    if i>sq:
        return 0
    if n%i==0:
        if i!=n//i:
            v=n//i
        v+=i
    i+=1
    return v+factors_sum(n)
print(factors_sum(n))
