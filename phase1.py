# Phase 1:
# Initial S box generation using Chaotic Logistic Map and Tent Map
# Chaotic Logistic Map: x[i+1] = ux[i](1-x[i])
# Tent Map: x[i+1] = x[i]/b,           0 < x[i] <=b
#                    (1-x[i])/(1-b),   b < x[i] < 1
# x0 = 15961/29589
# u  = 3.999
# b  = 0.499


from decimal import *
from math import floor
from functions import *
from performance import *

def generate_sbox():
    # Set precision to 20
    getcontext().prec = 15

    # Define intital/constant values
    x = Decimal(15961)/Decimal(29589)
    u  = Decimal(3999)/Decimal(1000)
    b = Decimal(4999)/Decimal(10000)

    print(x)
    print(u)
    print(b)

    # To counter Transient Effect
    # Iterate over Chaotic Logistic Map
    x = chaotic(x, u, 50)
    #print(x)

    # Iterate over Tent Map
    x = tent(x, b, 50)
    #print(x)

    # Generate S Box
    s = []
    while len(s) < 256:
##        t1 = int((float(x*(10**6)) - floor(x*(10**6)))*25)
##        t2 = int((float(x*(10**6)) - floor(x*(10**6)))*14)
        x = chaotic(x, u, 25)
        x = tent(x, b, 14)
        #n = int(floor(256*x))
        n = int((float(x*(10**6)) - floor(x*(10**6)))*256)
        if n not in s:
            #print(len(s))
            #print(s)
            s.append(n)
    return s


#if __name__ == '__main__':
#    s = generate_sbox()
#    print(pretty(s))
#    print(is_bijective(s))

#Mean: 107.5

s1 = [78,224,103,81,237,62,159,185,93,96,90,222,232,252,66,154,
     0,43,213,28,246,8,84,22,238,83,92,184,58,211,99,233,
     181,161,210,56,19,130,30,152,157,190,162,163,141,167,12,245,
     53,216,119,178,126,235,127,244,9,50,121,231,54,98,200,40,
     145,13,71,68,110,27,63,124,75,85,172,243,158,188,39,4,
     129,201,45,197,187,179,113,60,6,170,1,89,59,49,221,111,
     174,186,74,131,241,67,229,220,116,194,25,136,144,214,115,44,
     156,20,123,118,137,3,7,219,70,234,135,138,104,33,228,97,
     180,46,176,109,155,16,151,65,77,227,51,37,148,36,101,254,
     42,193,55,240,31,52,166,114,82,73,202,183,230,2,255,215,
     34,86,112,203,171,5,147,120,80,189,106,134,87,175,168,250,
     133,29,236,208,143,105,38,117,239,209,160,100,79,253,206,165,
     196,35,173,125,140,199,23,242,47,32,191,102,17,61,108,122,
     223,204,95,251,57,64,91,72,94,225,153,69,248,24,26,146,
     48,107,10,198,218,212,192,41,18,15,182,150,247,132,11,217,
     207,164,205,249,149,169,21,226,177,195,14,88,142,139,76,128]

#Mean: 105.75
s2 = [161,41,0,247,163,32,150,214,169,122,189,248,61,102,104,75,
      70,203,197,124,142,132,221,53,243,225,98,121,233,36,234,46,
      95,116,54,71,107,55,143,49,45,65,192,141,182,79,64,183,
      56,184,119,186,92,73,217,117,110,129,140,139,162,137,198,72,
      115,90,108,20,29,13,42,33,219,205,187,22,216,245,12,235,
      84,101,120,28,138,69,224,109,202,204,9,10,144,218,196,244,
      114,77,210,232,30,165,222,123,128,176,135,172,91,130,37,246,
      31,231,148,94,180,178,154,88,87,38,160,6,131,14,118,81,
      179,100,103,60,157,226,19,89,158,105,74,251,208,26,173,134,
      125,126,164,149,43,223,52,27,39,51,153,133,85,238,8,127,
      240,63,207,47,156,239,193,48,3,209,253,50,175,5,62,168,
      97,201,67,215,16,25,146,167,35,68,57,111,242,185,220,96,
      229,15,188,106,155,76,145,230,136,250,199,59,66,249,228,78,
      191,181,40,255,206,213,113,152,80,190,58,171,212,17,18,112,
      147,227,241,21,174,200,1,44,195,93,82,151,170,194,11,252,
      166,211,23,7,159,177,237,86,34,254,4,83,99,2,24,236]
      
#Mean: 109
s3 = [240,136,196,3,97,186,117,49,180,146,36,209,14,21,12,39,
      167,179,116,40,227,51,8,89,243,108,130,215,160,244,217,66,
      91,74,126,70,75,141,183,238,73,156,128,45,77,56,61,1, 
      92,119,113,111,201,149,205,4,173,64,33,94,172,7,50,30,
      0,202,110,232,2,150,147,170,187,63,47,10,55,5,82,86,
      233,228,52,184,9,112,99,197,38,195,22,25,230,24,253,212,
      158,100,41,54,68,18,71,19,76,140,79,88,59,101,178,210,
      78,194,199,192,237,83,163,102,193,218,254,131,248,6,231,198,
      106,46,190,67,53,234,62,174,203,207,252,125,159,32,95,115,
      17,80,148,162,229,225,118,153,189,255,23,122,235,121,104,134, 
      87,164,142,211,93,107,15,124,139,151,69,206,161,98,249,169,
      182,31,175,135,20,60,109,81,96,176,236,204,250,44,90,37, 
      85,251,213,177,221,208,43,155,105,137,28,13,143,181,65,72, 
      34,133,132,154,157,222,120,171,216,241,123,188,245,144,219,129, 
      223,191,29,138,242,224,239,42,247,35,168,58,246,145,185,48, 
      26,214,166,16,114,200,127,226,57,165,84,103,220,11,27,152]
      
s = generate_sbox()
print(s)
print(pretty(s))
print(is_bijective(s))
print((nonlinearity(s)))
s = test_nonlinearity(s)
x=0
print(s)
for i in s:
    x += i
    
x /= len(s)
print("Non linearity: {}" . format(x))
