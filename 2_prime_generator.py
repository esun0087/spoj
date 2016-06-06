
prime_len = 32000
prime_tmp = [True for i in range(prime_len)]
prime_tmp[0] = prime_tmp[1] = False
from math import sqrt

for i in range(2, int(sqrt(prime_len)) + 1):
    if prime_tmp[i]:
        for j in range(i*i, prime_len, i):
            prime_tmp[j] = False
prime = [i for i in range(prime_len) if prime_tmp[i]]

t = int(input())
for i in range(t):
    test_len = 100001
    line = input()
    m, n = line.split()
    m, n = int(m), int(n)
    be_prime = [True for i in range(test_len)]
    for p in prime:
        if p * p > n:
            break
        start = p - m % p
        if start % p == 0:
            start = 0
        if (start + m) // p == 1:
            start += p
        for j in range(start, test_len, p):
            be_prime[j] = False
    for i in range(n-m+1):
        if be_prime[i]:
            if i + m != 1:
                print (i + m)
        