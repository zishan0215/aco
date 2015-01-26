# Phase 1:
# Initial S box generation using Chaotic Logistic Map
# and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.99999999999999999999
# b  = 0.49999999999999999999


from decimal import *
from random import randint
from math import floor

# Set precision to 20
getcontext().prec = 20

# Define intital/constant values
x = Decimal(15961)/Decimal(29589)
u  = Decimal(39999999999999999999)/Decimal(10000000000000000000)
b = Decimal(4999999999999999999)/Decimal(10000000000000000000)

print x
print u
print b

# Iterate over Chaotic Logistic Map
for i in range(50):
    x = u*x*(1-x)

print x

# Iterate over Tent Map
for i in range(50):
    if 0 < x and x <= b:
        x = x/b
    elif b < x and x < 1:
        x = (1-x)/(1-b)
    else:
        print "Something wrong at Tent Map"

print x

s = []
count = 0
while len(s) != 255:
    n = randint(0,255)
    n = int(floor(n*x))
    if n not in s:
        count += 1
        print count
        print s
        s.append(n)