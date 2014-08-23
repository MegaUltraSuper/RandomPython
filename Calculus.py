#Calculus Functions

#example functions
# F(x) = x^2
def parabola(x):
    return x*x
# F(x) = 2x+1
def line(x):
    return 2*x
# F(x) = x^4-3x^3+x-10
def poly(x):
    return x*x*x*x-3*x*x*x+x-10

#Integration between (a,b), where F is some function
#n = number of trapezoids
#Trapezoidal Approx
def ATrap(a,b,F,n=10000):
    Area = 0
    w = (b-a)/n
    for num in range(1,n+1):
        h1 = F(a+ w*(num-1))
        h2 = F(a+ w*num)
        Area += h1*w-1/2*(h2-h1)*w
    return Area
