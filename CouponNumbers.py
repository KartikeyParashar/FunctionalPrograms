# a. Desc ­> Given N distinct Coupon Numbers, how many random numbers do you
# need to generate distinct coupon number? This program simulates this random
# process.
# b. I/P ­> N Distinct Coupon Number
# c. Logic ­> repeatedly choose a random number and check whether it's a new one.
# d. O/P ­> total random number needed to have all distinct numbers.
# e. Functions => Write Class Static Functions to generate random number and to
# process distinct coupons.

from random import randint
coupons_want = int(input("How many distinct coupon number you want to generate: "))
i=0
randomNumbersGenerated=0
random_number = randint(1,coupons_want)
temp =[]
while i<coupons_want:
    randomNumbersGenerated += 1
    if random_number not in temp:
        temp.append(random_number)
        i+=1
    random_number = randint(1, coupons_want)
    print(temp)
print(f"For {coupons_want} unique coupons,we have to generate {randomNumbersGenerated} distinct random numbers")
