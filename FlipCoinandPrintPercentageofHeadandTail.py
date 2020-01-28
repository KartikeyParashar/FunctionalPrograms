from random import randint
n = int(input("How many times you want to Flip a coin: "))
heads=0
tails=0
for i in range(n):
    result=randint(0,1)
    if result==0:
        heads+=1
    else:
        tails+=1
percentheads=(heads*100)/n
percenttails=(tails*100)/n
print(f"Percentage of heads:{round(percentheads,2)}%")
print(f"Percentage of heads:{round(percenttails,2)}%")