import random
#Calculus Functions

#example functions

l1 = [1,1,1,1,1,2]
l2 = [0]*1000
for i in range(1000):
    l2[i]=random.randrange(0,100)

def parabola(x):
    """F(x) = x^2"""
    return x*x

def line(x):
    """F(x) = 2x"""
    return 2*x

def poly(x):
    """F(x) = x^4-3x^3+x-10"""
    return x*x*x*x-3*x*x*x+x-10

def trap(a,b,F,n=10000):
    """Integration between (a,b), where F is some function
    n = number of trapezoids
    Trapezoidal Approx"""
    Area = 0
    w = (b-a)/n
    for num in range(1,n+1):
        h1 = F(a+ w*(num-1))
        h2 = F(a+ w*num)
        Area += h1*w-1/2*(h2-h1)*w
    return Area

def mid(a,b,F,n=10000):
    """Integration between (a,b), where F is some function
    n = number of rectangles
    Midpoint Approx"""
    Area = 0
    w = (b-a)/n
    for i in range(1,n+1):
        h = F(a+w*(i+1/2))
        Area += h*w
    return Area

def right(a,b,F,n=10000):
    """Integration between (a,b), where F is some function
    n = number of rectangles
    Right Approx"""
    Area = 0
    w = (b-a)/n
    for i in range(0,n):
        h = F(a+w*i)
        Area += h*w
    return Area

def left(a,b,F,n=10000):
    """Integration between (a,b), where F is some function
    n = number of rectangles
    Left Approx"""
    Area = 0
    w = (b-a)/n
    for i in range(1,n+1):
        h = F(a+w*i)
        Area += h*w
    return Area

def mean(A):
    """calculates the mean of list A"""
    return sum(A)/len(A)

def variance(A):
    """calculates the variance of A"""
    m = mean(A)
    v = 0
    for x in A:
        v += ((x-m)*(x-m))
    return v/(len(A)-1)

def stddev(A):
    """calcs standard deviation"""
    v = variance(A)
    return sqroot(v)

def sqroot(num):
    """method for approx a square root
    making it up as I go
    max of 10^10 with precision to 10^-10"""
    temp = 0
    for i in range(20):
        temp += getdigit(i,num, temp)
    return temp

def getdigit(place,num,temp):
    """helper to sqroot"""
    power = 10-place
    for index in range(1,11):
        if pow(temp+ index*pow(10, power),2) > num:
            return (index-1)*pow(10,power)  

def square(num):
    """calculating a decimal squared using int
    (exact up to 2 decimal places)  O(num*p)
    honestly not very good"""
    n = int(num*100+.1)
    print(n)
    s = 0
    for i in range(n):
        s += 1+2*i
    return s/10000

