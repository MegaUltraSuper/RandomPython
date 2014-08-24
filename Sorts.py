import random
import time
import math

# sorting algorithms that return exec time

# test List
List = [2,3,1,10,9,5,8,4,7,6]
a = 100
b = 400
c = 2000
d = 50000
e = 50000
List1 = [0]*a
List2 = [0]*b
List3 = [0]*c
List4 = [0]*d
List5 = [0]*e
for i in range(a):
    List1[i] = random.randrange(0,1000)
for i in range(b):
    List2[i] = random.randrange(0,1000)
for i in range(c):
    List3[i] = random.randrange(0,1000)
for i in range(d):
    List4[i] = random.randrange(0,1000)
for i in range(d):
    List5[i] = random.randrange(0,1000000)


def bubble(A, desc = False, display = False):
    """Sorts array A using bubble sort algorthim
    O(n^2) complexity"""
    start = time.clock()
    for iteration in range(1,len(A)):
        for index in range(0,len(A)-iteration):
            if desc==False:
                if A[index] > A[index+1]:
                    num = A[index]
                    A[index] = A[index+1]
                    A[index+1] = num
            else:
                if A[index] < A[index+1]:
                    num = A[index]
                    A[index] = A[index+1]
                    A[index+1] = num
        end = time.clock()
        if end-start > 6:
            return ">6"
    end = time.clock()
    if display == True:
        print(A)
    return end-start

def comb(A, desc = False, display = False):
    """Sorts array A using comb sort algorthim
    based of of bubble sort, should be faster"""
    start = time.clock()
    gap = int(len(A)/1.5)
    for iteration in range(1,len(A)):
        for index in range(0,len(A)-iteration):
            if gap < 1:
                gap = 1
            if desc==False:
                if A[index] > A[index+gap]:
                    num = A[index]
                    A[index] = A[index+gap]
                    A[index+gap] = num
            else:
                if A[index] < A[index+gap]:
                    num = A[index]
                    A[index] = A[index+gap]
                    A[index+gap] = num
            gap -= 1
        end = time.clock()
        if end-start > 6:
            return ">6"
    end = time.clock()
    if display == True:
        print(A)
    return end-start

def stooge(A,i,j, display=False):
    """Sorts array A using stooge sort algorthim
    stupidly very inefficient O(n^2.7)
    never use EVER"""
    start = time.clock()
    message = ""
    message=stooges(A,i,j,start)
    if message == ">6":
        return ">6"
    if display == True:
        print(A)
    end = time.clock()
    return end-start

def stooges(A,i,j, start):
    i=int(i)
    j=int(j)
    if A[j] < A[i]:
        num = A[j]
        A[j] = A[i]
        A[i] = num
    if (j-i+1) > 2:
        t = (j-i+1)/3
        end = time.clock()
        if end-start > 6:
            return ">6"
        stooges(A,i,j-t,start)
        end = time.clock()
        if end-start > 6:
            return ">6"
        stooges(A,i+t,j,start)
        end = time.clock()
        if end-start > 6:
            return ">6"
        stooges(A,i,j-t,start)
        end = time.clock()
        if end-start > 6:
            return ">6"
    return ""

def count(A, k=1000, display=False, desc = False):
    """Sorts array A using count sort algorthim
    very efficient for small-medium K O(n+k),
    k is the range of possible integers"""
    start = time.clock()
    C = [0]*k
    for num in A:
        C[num]+=1
    placeinA=0
    placeinC=0
    for amount in C:
        for index in range(0,amount):
            A[placeinA] = placeinC
            placeinA += 1
        placeinC += 1
        end = time.clock()
        if end-start > 6:
            return ">6"
    end = time.clock()
    if display == True:
        print(A)
    return end - start

#copy, split, and m are helper functions for merge method
def merge(A, display = False):
    """Sorts array A using merge sort algorthim
    very efficient  O(nlog(n))"""
    start = time.clock()
    B = [0]*(len(A))
    n = len(A)
    split(A, 0, n, B)
    end = time.clock()
    if display == True:
        print(A)
    return end-start

def copy(B,i,j,A):
    i=int(i)
    j=int(j)
    for num in range(i,j):
        A[num]=B[num]
    return A


def split(A, i, j, B):
    i=int(i)
    j=int(j)
    if(j-i < 2):                       
        return                                 
    mid = int((j+i)/2)
    split(A,i,mid,B)
    split(A,mid,j,B)
    m(A,i,mid,j,B)
    A = copy(B,i,j,A)
 
def m(A,i,mid,j,B):
    i=int(i)
    j=int(j)
    i0 = i
    i1 = mid
    i0=int(i0)
    i1=int(i1)
    for num in range(i,j):
        if i0 < mid and (i1 >= j or A[i0] <= A[i1]):
            B[num] = A[i0]
            i0 = i0 + 1
        else:
            B[num] = A[i1]
            i1 = i1 + 1
    return
 
def test(A):
    """tries various sort methods on list A and
    returns results"""
    bb,cm,cnt,me = 0,0,0,0
    maximum = max(A)
    bb = str(bubble(A))
    print("Bubble Sort: " +bb+ " seconds")
    cm = str(comb(A))
    print("Comb Sort: " +cm+ " seconds")
    cnt = str(count(A,k=maximum+1))
    print("Count Sort: " +cnt+ " seconds")
    me = str(merge(A))
    print("Merge Sort: " +me+ " seconds")

          
