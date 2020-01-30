from random import randint


print("Welcome to tic tac toe Game: ")
name = input("Type your name: ")

print(f"In this Game: Player 1 is {name} and player 2 is Computer")

#set player to 1
player = 1

# Set the initial state
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def show_state(state):
  print(state[0], state[1], state[2])
  print(state[3], state[4], state[5])
  print(state[6], state[7], state[8])

# 0/1/2
# 3/4/5
# 6/7/8

def win_status(state, player):
  if state[0] == player and state[1] == player and state[2] == player:
    return 'win'
  if state[3] == player and state[4] == player and state[5] == player:
    return 'win'
  if state[6] == player and state[7] == player and state[8] == player:
    return 'win'
  if state[0] == player and state[3] == player and state[6] == player:
    return 'win'
  if state[1] == player and state[4] == player and state[7] == player:
    return 'win'
  if state[2] == player and state[5] == player and state[8] == player:
    return 'win'
  if state[0] == player and state[4] == player and state[8] == player:
    return 'win'
  if state[2] == player and state[4] == player and state[6] == player:
    return 'win'  

  for position in range(9):
    if state[position] == 0:
      return
  return 'Draw'

possible_places = [0, 1, 2, 3, 4, 5, 6, 7, 8] 

while True:
  # Get Valid Move
  print(f"Player {player}: ")
  while True:
    if player==1:
      move = int(input("What is your move?: "))
      if move in possible_places:
        break
      print("Illegal Move")
    else:
      move = randint(0,8)  
      if move in possible_places:
        break
    

  # delete that move from possible_places
  possible_places[move]=-1 

  # update the state
  state[move] = player
  
  # show the state
  show_state(state)

  # check win status - win,loose,draw
  status = win_status(state, player)
  if status == 'win':
    print(f"Player {player} wins")
    break

  # switch players 2->1 , 1->2 
  if player == 1:
    player = 2
  else:
    player = 1
    
show_state(state)
print("Game is over")    
