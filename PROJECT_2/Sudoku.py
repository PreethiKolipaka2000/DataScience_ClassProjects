# PROGRAM        : CREATING A SUDOKU PUZZLE GAME USING NUMPY AND OOPS COONCEPT
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 03-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 


import numpy as np
import sys
sudoku = []
print("--------------Enter the unsolved puzzle !! please keep 0 for unsolved blanks---------------")
# Reading Unsolved Sudoku Puzzle From The User 
for i in range(9):
    a=list(map(int,input().split()))
    sudoku.append(a)
sudoku=np.matrix(sudoku)
print("---------Given Unsolved Puzzle------")
print(sudoku)
def disp(a):
    print("-------------------------")
    for i in range(9):
        for j in range(9):
            if(j==2 or j==5 or j==8):
                print(a[i,j],end=" | ")
            elif(j==0):
                print("|",a[i,j],end=" ")
            else:
                print(a[i,j],end=" ")
        print()
        if(i==2 or i==5 or i==8):
            print("-------------------------")
    #print("-----------------------")
# Checking Whether to place that element in that row and column
def is_possible(r,c,num):
    global sudoku 
    # Checking whther the number is present in tha given row 
    for i in range(0,9):
        if(sudoku[r,i]==num):
            return False 
    # Checking whther the number is present in tha given column
    for i in range(0,9):
        if(sudoku[i,c]==num):
            return False 
    # Checking the number is in 3x3 box of given row and column 
    x=(r//3)*3 
    y=(c//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if(sudoku[x+i,y+j]==num):
                return False 
    return True 

# Solving Puzzle for every element in the 9x9 cells
def solve_puzzle():
    for i in range(0,9):
        for j in range(0,9):
            # if the position is Empty and checking which element among 1-9 is possible to place 
            # if possible place the element and else backtrack
            if(sudoku[i,j]==0):
                for num in range(1,10):
                    if(is_possible(i,j,num)):
                        sudoku[i,j]=num 
                        solve_puzzle()
                        sudoku[i,j]=0 
                return 
    # Displaying Solutions
    disp(sudoku)
    #print(sudoku)
    ip=input("-----------Do You Want More Solutions For the puzzle  ???  if Not Press 'N' ")
    if(ip=='N'):
        sys.exit()
solve_puzzle()


        
