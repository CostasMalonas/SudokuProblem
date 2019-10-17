# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
               
incorrect6 = [[0,1,2], 
              [2,0,1], 
              [1,2,0]]  

incorrect7 = [ [2.5, 3, 1],
               [1, 2.5, 3],
               [3, 1, 2.5] ]
               

def find_freq(fr):
    freq = 9 * [0] 
    #for i in fr:
    for j in fr:
        freq[j - 1] = freq[j - 1] + 1
    return freq

def column(matrix, i):
    return [row[i] for row in matrix]
  
               
def check_sudoku(ls):
    for i in ls:
        if (all(isinstance(x, int) for x in i)) != True:
            return False
           
    length = len(ls)
    for i in ls:
        for j in i:
            if j > length or j <= 0:
                return False
    row = 0
    col = 0 
    while row < length:
        pin1 = ls[row]
        freqr = find_freq(pin1)
        row = row + 1
        for j in freqr:
            if j > 1:
                return False
    j = 0  
    i = 0
    #while j < length:                
    while i < length:
        pin = column(ls, i)
        i = i + 1
        freqc = find_freq(pin)
        for n in freqc:
            if n > 1:
                return False
       # i = 0        
        #j = j + 1
    return True    
                
       
        
            
    
#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False

#print check_sudoku(incorrect7)
