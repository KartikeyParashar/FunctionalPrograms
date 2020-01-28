n=int(input("Enter the number upto which you want the Harmonic Series and its Sum: "))
sum=0
for i in range(1,n+1):
    sum+=(1/i)
    if i<n:
        print(f"1/{i} + ",end=" ")
    else:
        print(f"1/{i} = ",end=" ")
print(sum)