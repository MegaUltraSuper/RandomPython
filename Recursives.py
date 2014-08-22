#various recursive algorithms

#quick exponentiation of integers
def AExp(n,p):
    if p==0:
        return 1
    elif p%2==1:
        return n*AExp(n,p-1)
    else:
        t = AExp(n,p/2)
        return t*t
    
#quick get greatest common denominator
def AGCD(a,b):
    if -.0001<a-b<.0001:
        return a
    elif a<b:
        return AGCD(b,a)
    elif a>b:
        print(a-b)
        return AGCD(b,a-b)
    else:
        return "no GCD"

#get nth Fibbonaci number
def AFib(n):
    if n <= 0:
        return 0
    if n <= 1:
        return 1
    else:
        return AFib(n-1)+AFib(n-2)

#Ackermann's Function
#total computable function that is not primitive recursive.
#sometimes used to benchmark compilers for deep recursion 
def AAckermann(a,b):
    if a == 0:
        return b+1
    elif a != 0 and b == 0:
        return AAckermann(a-1,1)
    else:
        return AAckermann(a-1, AAckermann(a,b-1))
