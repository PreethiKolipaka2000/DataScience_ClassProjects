# PROGRAM        : CREATE A TIC TAC TOE GAME USER VS USER USING NUMPY AND OOPS CONCEPT
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in
# DATE           : 03-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 


import numpy as np 
import random
#board = np.zeros(shape=(3,3),dtype=int)
class Tic_Tac_Toe:
    def __init__(self):
        self.board=[]
        #self.board=np.chararray((3,3))
    # Creating an Empty Board Matrix Using Numpy 
    def create_board(self):
        t=[]
        for i in range(3):
            r=['-','-','-']
            t.append(r)
        self.board=np.matrix(t,dtype=str)
    # Creating a Random Player initializing to Start the Game 
    def create_player(self):
        return random.randint(1,2)

    # Choosing and Fixing the position to be placed the item by the player
    def choose_place(self,r,c,p):
        self.board[r,c]=p 

    # Checking the player either wins the game with the current Move 
    def check_winning(self,player):

        # Checking The Rows FOr Winning 
        for i in range(len(self.board)):
            winner=True 
            for j in range(len(self.board)):
                if self.board[i,j]!=player:
                    winner=False 
                    break 
            if(winner):
                return True 
        # Checking The Columns FOr Winning
        for i in range(len(self.board)):
            winner=True 
            for j in range(len(self.board)):
                if self.board[i,j]!=player:
                    winner=False 
                    break 
        if(winner):
            return True 
            
        # Checking for diagonal 1 ->  1,5,9
        winner=True 
        for i in range(len(self.board)):
            if self.board[i,i]!=player:
                winner=False 
                break 
        if(winner):
            return True 
            
        # Checking for diagonaal 2 - > 3,5,7
        winner=True 
        for i in range(len(self.board)):
            if self.board[i,len(self.board)-i-1]!=player:
                winner=False 
                break
        if(winner):
            return True 
        return False 
        for i in self.board:
            for j in i:
                if j=='-':
                    return False 
        return True 
    # Checking Whether the Board if FIlled with the Moves or not 
    def check_filled(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i,j] =='-':
                    return False 
        return True 
    # Swapping the players to their chances and next player turn
    def swap(self,p):
        if(p=='X'):
            return 'O'
        return 'X'
    # Drawboard1 function displays the board in a  normal format
    def draw_board1(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(self.board[i,j],end=" ")
            print()
    # Drawboard Displays the borad in a a game format
    def draw_board(self):
        b=self.board.copy()
        for i in range(len(b)):
            for j in range(len(b)):
                if(b[i,j]=='-'):
                    b[i,j]=" "
            print(" "+str(b[i,0])+" "+"|"+" "+str(b[i,1])+" "+"|"+" "+str(b[i,2]))
            if(i!=len(b)-1):
                print("___|___|___")
            else:
                print("   |   |   ")
 
    def play(self):
        self.create_board()
        ch=self.create_player()
        if(ch==1):
            player='X'
        else:
            player='O'
        while(True):
            print("---------Player     "+player+"    TURN !!!!            --------------------------")
            self.draw_board1()
            print()
            self.draw_board()
            x,y=map(int,input("Enter Position to Place Your Place  your check !!!    ").split())
            print()

            self.choose_place(x-1,y-1,player)

            if(self.check_winning(player)):
                print("--------------Hurray --- Player-@@@----"+player+"---++-+-+++----WON THE GAME---+++---+++")
                break 
            if(self.check_filled()):
                print("--------------OOps Match Ended With a Tie.......")
                break 
            player=self.swap(player)
        print()
        self.draw_board1()

t=Tic_Tac_Toe()
p='Y'
while(p=='Y'):
    t.play()
    print("----Do You Want TO Play Again???------ If Yes Press 'Y'---- Else press'N'----")
    p=input()



