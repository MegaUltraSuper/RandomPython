#Calculus Functions

#example functions

def parabola(x):
    """F(x) = x^2"""
    return x*x

def line(x):
    """F(x) = 2x+1"""
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
    
