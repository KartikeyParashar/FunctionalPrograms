# a. Desc ­> Simulates a gambler who start with $stake and place fair $1 bets until
# he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
# times he/she wins and the number of bets he/she makes. Run the experiment N
# times, averages the results, and prints them out.
# b. I/P ­> $Stake, $Goal and Number of times
# c. Logic ­> Play till the gambler is broke or has won
# d. O/P ­> Print Number of Wins and Percentage of Win and Loss.

from random import randint

Stake = int(input("How much Stake do you want to place: "))
Goal = int(input("How much goal do you have after which you don/'t want to bet: "))
Number_of_times = int(input("How many total bets you want to play:  "))

wins = 0
loose = 0
Bets=0
while (Bets != Number_of_times and Stake > 0 and Stake != Goal):
  bet=randint(0,1)
  if bet > 0.5:
    wins += 1
    Stake += 1
  else:
    loose += 1
    Stake -= 1
  
  Bets+=1  

print(f"Winning Percentage: {(wins*100)/Number_of_times} and Loose Percentage: {(loose*100)/Number_of_times}")