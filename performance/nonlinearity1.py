# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:36:00 2015

@author: Zishan Ahmad
"""
from scipy.linalg import hadamard


def fwt(f):
    """
        Computes Fast Walsh Table
        f is a Boolean function represented as a TT of length 2^n
    """
    wf = []
    for x in f:
#        print(len(f))
        if x == 0:
            wf.append(1)
        else:  # Assume a proper truth table of only 1 or 0 entries
            wf.append(-1)
    k = 256
    n = 8
    sw = 1
    bs = k - 1
    while True:
        li = 0
        bs = bs >> 1
        for b in range(bs, -1, -1):
            ri = li + sw
            for p in range(0, sw):
                a = wf[li]
                for i in range(0, len(wf)):
                    print((i, wf[i]))  # Comment
                b = wf[ri]
                wf[li] = a + b
                wf[ri] = a - b
                li = li + 1
                ri = ri + 1
            li = ri
        sw = (sw << 1) & (k - 1)
        if (sw == 0):
            break
    return wf

def walsh_spectrum(f):
    x = f*hadamard(256)
    length = len(x)
    walsh = []
    for i in range(1,length):
        length_of_list=len(x[i])
        sum = 0
        for j in range(length_of_list):
            sum = sum + x[i][j]
        walsh.append(sum)
    return walsh

def bf_nonlinearity(f, n):
    """ Intermediate non linearity """
    #fw = fwt(f)
    fw = walsh_spectrum(f)
    for i in range(len(fw)):
        fw[i] = abs(fw[i])
    # nonlinearity from the Walsh transform
    return ((2 ** (n - 1)) - (max(fw) / 2))


def nonlinearity(S):
	""" Outputs the nonlinearity of the s box """
	order = len(S)
	n = 8
	nl = 1 << order  # over the top
	for mask in range(1, order):
		f = []
		for x in range(0, order):
			s = 0
			for i in range(0, n):
				if ((mask & (1 << i)) > 0) and ((S[x] & (1 << i)) > 0):
					s = s ^ 1;
			f.append(s)
			# print(f) # Comment
		bfnl = bf_nonlinearity(f, n)
		if (bfnl < nl):
			nl = bfnl
	return nl