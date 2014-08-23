#various recursive algorithms

def exp(n,p):
    """quick exponentiation of integers"""
    try:
        if p==0:
            return 1
        elif p%2==1:
            return n*exp(n,p-1)
        else:
            t = exp(n,p/2)
            return t*t
    except:
        return "could not calculate (nested too deep)"
    
def gcd(a,b):
    """quick get greatest common denominator"""
    try:
        if -.0001<a-b<.0001:
            return a
        elif a<b:
            return gcd(b,a)
        elif a>b:
            return gcd(b,a-b)
        else:
            return "no GCD"
    except:
        return "could not find GCD (nested too deep)"

def fib(n):
    """get nth Fibbonaci number"""
    try:
        if n <= 0:
            return 0
        if n <= 1:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    except:
        return "could not find "+n+"th fibbonaci number (nested too deep)"
    
def ackermann(a,b):
    """Ackermann's Function
    total computable function that is not primitive recursive.
    sometimes used to benchmark compilers for deep recursion"""
    try:
        if a == 0:
            return b+1
        elif a != 0 and b == 0:
            return ackermann(a-1,1)
        else:
            return ackermann(a-1, ackermann(a,b-1))
    except:
        return "nested too deep"

def fact(n):
    """returns n!"""
    try:
        if n <= 1:
            return 1
        else:
            return n*fact(n-1)
    except:
        return "could not find"

def n_fact(a):
    """returns 1!...n! corecursively"""
    n,f = 1,1
    while n <= a:
        yield f
        n,f = n+1,f*(n + 1)

def hanoi(n):
    """solves tower of hanoi for n stacks
    answer = 2^(n+1) - 1"""
    try:
        if n <= 1:
            return 1
        else:
            return 2*hanoi(n-1) +1
    except:
        return "could not solve"
    
    
