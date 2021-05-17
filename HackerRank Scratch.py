# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:41:45 2021

@author: sebas
"""

ab = [1,1,2,2,3,4,5,5,5,6,7,8,8,8]
nm = len(ab)

def sockMerchant(n, ar):
    qty = [ar.count(num) for num in list(set(ar))]
    pairs = [i//2 for i in qty]
    print(sum(pairs))
    return sum(pairs)
    
# =============================================================================
# sockMerchant(nm, ab)
# =============================================================================

#%%

# =============================================================================
# def countingValleys(n, path):
#     a = []
#     b = []
#     for i in path:
#         if i == 'U':
#             a.append(1)
#             if sum(a) == 0:
#                 b.append(1)
#         elif i == 'D':
#             a.append(-1)
#     print(sum(b))
# =============================================================================
        
path = 'DUDUUUDDDU'
n = len(path)

# =============================================================================
# def countingValleys(steps, path):
#     a = [0] * len(path)
#     b = [0] * len(path)
#     for i in range(len(path)):
#         if path[i] == 'U':
#             a[i] = 1
#             if sum(a) == 0:
#                 b[i] = 1
#         else:
#             a[i] = -1
#     print(sum(b))
#     
# =============================================================================

def countingValleys(steps, path):
    a = 0
    b = 0
    for i in path:
        if i == 'U':
            a += 1
            if a == 0:
                b += 1
        else:
            a -= 1
    return b

# =============================================================================
# countingValleys(n, path)
# =============================================================================

#%%
if n%2 == 0:
    if (n>=2 and n<=5) or (n>20):
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')
    
#%%

a = 3
b = 2

[print(i) for i in [a+b, a-b, a*b]]

#%%

def is_leap(year):
    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True
    else:
        leap = False
    print(leap)
    return leap

#%%

n=10

print(''.join(str(i) for i in list(range(1,n+1))))

#%%

a=3
b='07895462130'
c=919875641230
d=9195969878

def wrapper(func):
    def inner(*args):
        #func()
        print('+91 ', func(*args) )
    return inner

#@wrapper
def phone(n, *args):
    for i in args:
        if len(str(i)) > 1:            
            if len(str(i)) == 10:
                print('{} {}'.format(str(i)[0:5], str(i)[5:10]))
            elif str(i)[0:2] == '91':
                print('{} {}'.format(str(i)[2:7], str(i)[7:12]))
            else:
                print('{} {}'.format(str(i)[-10:-5], str(i)[-5:]))
        

#%%


wrapper(phone(a,b,c,d))

#print('\a')

#%%

a=3
b = '07895462130'
c = 919875641230
d = '9195969878'
e = '1234567890'

#print('{} {}'.format(e[0:5], e[5:10]))

print(str(c)[-10:])



#%%

N = int(input())
x = input().split(' ')
X = [int(i) for i in x]

mean = sum(X)/N

X.sort()
    
if N%2 == 0:
    a = X[(N//2)-1]
    b = X[N//2]
    median = (b + a) / 2
else:
    median = X[(N//2)]
    
freq = [X.count(i) for i in X]

my_dict = dict(list(zip(X, freq)))
    
#print(my_dict)

mymax = 0 
mode = 0
for i in my_dict:
    if my_dict[i] > mymax:
        mymax = my_dict[i]
        mode = i
        
#print(mymax, mode)

print(X, '\n', mean, '\n', median, '\n', mode)
    
#%%dot 

def weightedMean(X, W):
    a = []
    for i in range(len(X)):
        a.append(X[i] * W[i])
    b = round(sum(a)/sum(W),1)    
    print(b)
        
y = [14,23,37,48,54]        
z = [1,1,3,1,1]     

weightedMean(y,z)

#%%
import math

y = [2,5,2,7,4]

def stdDev(arr):
    n = len(arr)
    mean = sum(arr)/n
    a = []
    for i in arr:
        a.append(round((i-mean)**2,1))
    b = math.sqrt(sum(a)/n)
    print(b)
    #print(sum(a), '\n', b, '\n', n)
        
stdDev(y)

#%%

y = '3 7 8 5 12 16 18 21'.split(' ')
y = [int(i) for i in y]

def quartiles(arr):
    n = len(arr)
    arr.sort()
    
    b = arr[:n//2]
    c = len(b)
                        
    if n%2 == 0:
        second = (arr[n//2-1] + arr[n//2]) / 2
        d = arr[n//2:]
        if c%2 ==0:
            first = (b[c//2-1] + b[c//2]) / 2
            third = (d[c//2-1] + d[c//2]) / 2
        else:
            first = b[c//2]
            third = d[c//2]
    else:
        second = arr[n//2]
        d = arr[(n//2)+1:]
        if c%2 == 0:
            first = (b[c//2-1] + b[c//2]) / 2
            third = (d[c//2-1] + d[c//2]) / 2
        else:
            first = b[c//2]
            third = d[c//2]    
        
    a = [first, second, third]
       
    print(arr, '\n', a, '\n', b, '\n', d)
    
quartiles(y)
    
#%%

y = '10 40 30 50 20'.split(' ')
y = [int(i) for i in y]
z = '1 2 3 4 5'.split(' ') 
z = [int(i) for i in z]

def interQuartile(values, freqs):
    
    a = [[values[i]]*freqs[i] for i in range(len(values))]
# =============================================================================
#     b = []
#     for i in a:
#         for j in i:
#             b.append(j)
# =============================================================================
    b = [j for i in a for j in i]
    b.sort()
    
    n = len(b)
    c = b[:n//2]
    e = len(c)
    
    if n%2 == 0:        
        d = b[n//2:]
        if e%2 == 0:
            first = (c[e//2-1] + c[e//2]) / 2
            third = (d[e//2-1] + d[e//2]) / 2
        else:
            first = c[e//2]
            third = d[e//2]
    else:
        d = b[n//2+1:]
        if e%2 == 0:
            first = (c[e//2-1] + c[e//2]) / 2
            third = (d[e//2-1] + d[e//2]) / 2
        else:
            first = c[e//2]
            third = d[e//2]
            
    f = third - first
                    
    #print(b, len(b), '\n', c, len(c), first, '\n', d, len(d), third, '\n', f)
    print(f'{f:.1f}')
    
interQuartile(y, z)

#%%

p1 = '0 0 1 1'.split(' ')
p2 = '1 1 2 2'.split(' ')

 

def findPoint():
    n = input()
    
    for i in range(int(n)):
        pp = input().rstrip().split(' ')
        p = [int(j) for j in pp]
        px = p[0]
        py = p[1]
        qx = p[2]
        qy = p[3]    
        dx = qx - px
        dy = qy - py
        rx = qx + dx
        ry = qy + dy
    #a = [rx,ry]
    #print(a)
        print(rx, ry)
    
findPoint()


#%%

def findPoint(px, py, qx, qy):   
    dx = qx - px
    dy = qy - py
    rx = qx + dx
    ry = qy + dy
    #a = [rx,ry]
    #print(a)
    print(rx, ry)
    
findPoint(0,0,1,1)
