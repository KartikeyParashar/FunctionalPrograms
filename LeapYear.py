year = int(input("Enter the year you want to check that Leap Year or not: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Yes it is a Leap Year")
        else:
             print("Not a Leap Year")
    else:
        print("Yes it is a Leap Year")

else:
    print("No its not a Leap Year")