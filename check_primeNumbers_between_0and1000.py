# Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range.

import math

# Store all prime numbers in empty list
prime_numbers = []


for i in range(2,1000):
    flag=0
    for j in range(2,int(math.sqrt(i+1))+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        prime_numbers.append(i)

print(prime_numbers)

