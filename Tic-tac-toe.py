#_________      _____      _________    _      ______         _______  _____   ____
#    |     |   |               |       / \    |                  |    |     | |
#    |     |   |       -       |      /---\   |          -       |    |     | |----
#    |     |   |_____          |     /     \  |______            |    |_____| |____


#create display board
#Take input from user if they want to be O or x and display player1 player2 chosen symbol
#Start game-X goes first-fill user value on board
#check if space is empty or not
 #-if empty continue
 #-if not empty -check for win/draw and display result
#restart if user wants to play it again
#compile all
# 1 2 3
# 4 5 6
# 7 8 9
#modules
#1-display board

def display(XO_board):
    print(XO_board[1]+"|"+XO_board[2]+"|"+XO_board[3])
    print(XO_board[4]+"|"+XO_board[5]+"|"+XO_board[6])
    print(XO_board[7]+"|"+XO_board[8]+"|"+XO_board[9])    
#2-XorO
def players(ok,player_1,player_2):
    if(ok):
        print(player_1 + ":X")
        print(player_2 + ":O")

#3
def full_board(board):

    if (XO_board[1]!=" " and XO_board[2]!=" " and XO_board[3]!=" "\
        or XO_board[4]!=" " and XO_board[5]!=" " and XO_board[6]!=" "\
        or XO_board[7]!=" " and XO_board[8]!=" " and XO_board[9]!=" "):
        return True
#4
def space_check(board,position):
    return (board[position]==" ")

def win_check():
    if(    XO_board[1]=='X' and XO_board[2]=='X' and XO_board[3]=='X'\
        or XO_board[4]=='X' and XO_board[5]=='X' and XO_board[6]=='X'\
        or XO_board[7]=='X' and XO_board[8]=='X' and XO_board[9]=='X'\
        or XO_board[1]=='X' and XO_board[4]=='X' and XO_board[7]=='X'\
        or XO_board[2]=='X' and XO_board[5]=='X' and XO_board[8]=='X'\
        or XO_board[3]=='X' and XO_board[6]=='X' and XO_board[9]=='X'\
        or XO_board[1]=='X' and XO_board[5]=='X' and XO_board[9]=='X'\
        or XO_board[3]=='X' and XO_board[5]=='X' and XO_board[7]=='X'\
        or XO_board[1]=='O' and XO_board[2]=='O' and XO_board[3]=='O'\
        or XO_board[4]=='O' and XO_board[5]=='O' and XO_board[6]=='O'\
        or XO_board[7]=='O' and XO_board[8]=='O' and XO_board[9]=='O'\
        or XO_board[1]=='O' and XO_board[4]=='O' and XO_board[7]=='O'\
        or XO_board[2]=='O' and XO_board[5]=='O' and XO_board[8]=='O'\
        or XO_board[3]=='O' and XO_board[6]=='O' and XO_board[9]=='O'\
        or XO_board[1]=='O' and XO_board[5]=='O' and XO_board[9]=='O'\
        or XO_board[3]=='O' and XO_board[5]=='O' and XO_board[7]=='O'):
        return True
        





#main began

not_bored=True   
while (not_bored):
 print("Welcome to tic-tac-toe")
 player_1=input("Enter player 1 name:")
 player_2=input("Enter player 2 name:")
 players(1,player_1,player_2)
 print("Game_Started")
 XO_board=[" "]*10
 display(XO_board)

 #players(0,player_1,player_2)
 game_on=True
 turn=1

 while(game_on):
      print("Enter position:")
      position=int(input())
      if(space_check(XO_board,position)):
        if(turn):
            XO_board[position]='X'
            display(XO_board)
            turn=0
            if win_check():
              game_on=False
              ok=1
              print("Congratulations "+ player_1+", you won the match")
        else:
            XO_board[position]='O'
            display(XO_board)
            turn=1
            ok=1
            if win_check():
              game_on=False
              print("Congratulations "+ player_2+", you won the match")
      else:
        if(full_board(XO_board)):
         print("Oops! Draw")
         break
      
        
    
 play_again=input("Want to play again?Y/N")
 if play_again.lower()[0]=='y':
    not_bored=True
 else:
    not_bored=False
    print("thanks for playing, hope you enjoyed the game!")



    






