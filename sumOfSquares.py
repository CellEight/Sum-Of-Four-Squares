from math import *
import sys
primes = [2,3,5,7,11,13,17,19,23
,29,31,37,41,43,47,53,59,61,67
,71,73,79,83,89,97,101,103,107,109
,113,127,131,137,139,149,151,157,163,167
,173,179,181,191,193,197,199,211,223,227
,229,233,239,241,251,257,263,269,271,277
,281,283,293,307,311,313,317,331,337,347
,349,353,359,367,373,379,383,389,397,401
,409,419,421,431,433,439,443,449,457,461
,463,467,479,487,491,499,503,509,521,523
,541,547,557,563,569,571,577,587,593,599
,601,607,613,617,619,631,641,643,647,653
,659,661,673,677,683,691,701,709,719,727
,733,739,743,751,757,761,769,773,787,797
,809,811,821,823,827,829,839,853,857,859
,863,877,881,883,887,907,911,919,929,937
,941,947,953,967,971,977,983,991,997]

def prime_factorize(n):
    if n in primes and n < 1000:
        return [[n,1]]
    elif n >= 1000:
        prime = True
        for p in primes:
            if n%p == 0:
                prime = False
                break
            if p > sqrt(n):
                break
        if prime:
            return [[n,1]]
    factors = []
    max = floor(n/2)
    for p in primes:
        if p > max:
            break
        if n%p == 0:
            i = 0
            while n%p == 0:
                i += 1
                n = floor(n/p)
            factors.append([p,i])
    return factors

def s2s_check(n):
    factors = prime_factorize(n)
    #print(factors)
    for factor in factors:
        if factor[0]%4 == 3 and factor[1]%2 == 1:
            return False
    return True

def s3s_check(n):
    if n == 0:
        return True
    if n%4 == 0:
        while n%4 == 0:
            n = int(n/4)
    if n%8 == 7:
        return False
    else:
        return True

def s4s_check(n):
    x1 = floor(sqrt(n))
    if n-x1**2 != 0:
        while not s3s_check(n-x1**2):
            x1 -= 1
            if x1 == 0:
                print('error')
        x2 = floor(sqrt(n-x1**2))
        if n-x1**2-x2**2 !=0:
            while not s2s_check(n-x1**2-x2**2):
                x2 -= 1
                if x2 == 0:
                    print('error')
            x3 = floor(sqrt(n-x1**2-x2**2))
            if n-x1**2-x2**2-x3**2 != 0:
                while floor(sqrt(n-x1**2-x2**2-x3**2))**2 != n-x1**2-x2**2-x3**2:
                    x3 -= 1
                    if x3 == 0:
                        print('error')
                x4 = int(sqrt(n-x1**2-x2**2-x3**2))
            else:
                x4 = 0
        else:
            x3 = 0
            x4 = 0
    else:
        x2 = 0
        x3 = 0
        x4 = 0
    print(n,'=',str(x1)+'^2 +',str(x2)+'^2 +',str(x3)+'^2 +',str(x4)+'^2')
    if n==x1**2+x2**2+x3**2+x4**2:
        pass
    else:
        print(WARNING)
        quit()

#s4s_check(int(sys.argv[1]))
for n in range(1, 10**3 + 1):
    s4s_check(n)
