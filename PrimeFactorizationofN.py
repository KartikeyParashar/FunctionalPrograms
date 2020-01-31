# Desc ­> Computes the prime factorization of N using brute force.
# I/P ­> Number to find the prime factors
# Logic ­> Traverse till i*i <= N instead of i <= N for efficiency .
# O/P ­> Print the prime factors of number N.

import math
n = int(input("Enter the number for which you want the prime factors: "))

def prime_factorization(n):
    while n%2==0:
        print(2)
        n=n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            print(i)
            n=n/i

    if n>2:
        print(n)

prime_factorization(n)
