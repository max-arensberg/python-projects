# pebble collector completed code with memoization and tabulation
import numpy as np

#Make a field based on user input rows and columns with 1s representing pebbles and 0s representing empty.
#There is no need to alter this functions code
def make_field(field, rows, cols):
    r = 0       
    while(r < rows):
        temp = []
        c = 0 
        while(c < cols):
            num = np.random.randint(2)
            temp.append(num)
            c += 1
        field.insert(r, temp)
        r += 1

    
#Show a list in a grid format
def display(list, cols, name):
    r = 0
    print("\n\n", name, "\n")
    print(" ---" * cols)
    while(r < len(list)):
        c = 0
        while(c < len(list[0])):
            print("|", list[r][c], end = " ")
            c += 1
        print("|")
        print(" ---" * cols)
        r += 1

#Initialize a table with -1 for a user-given number of rows and columns
def make_table(table, rows, cols):
    r = 0
    while(r < rows):
        temp = []
        c = 0
        while(c < cols):
            temp.append(-1)
            c += 1
        table.insert(r, temp)
        r += 1

#Recursive function to find maximum numbers of pebbles which can be collected in one pass using Memoization.
def max_collect_memo(field, r, c, info_table):
    if r < 0 or c < 0:                              # base case if cell is out of range
        return 0

    if info_table[r][c] != -1:                      # check if cell has already been memoized
        return info_table[r][c]                   # if it has, return value stored in cell

    left = max_collect_memo(field, r, c - 1, info_table)  # get value in cell to left
    above = max_collect_memo(field, r - 1, c, info_table)  # get value in cell above

    info_table[r][c] = max(left, above) + field[r][c]  # update info_table based on max value 
    return info_table[r][c]                            # return updated pebble count


#Recursive function to find maximum numbers of pebbles which can be collected in one pass using Tabulation.
def max_collect_tab(field, rows, cols, tab_table):
    if rows < 0 or cols < 0:     # base case for empty table
        return 0

    tab_table[0][0] = field[0][0]  # smallest known sub problem, no previous cells to count


    j = 1                       # initialize j at 1
    while j <= cols - 1:        # while loop  to keep j within bounds of matrix
        tab_table[0][j] = tab_table[0][j - 1] + field[0][j] # smallest unsolved subproblem
        j += 1    # increase j by 1


    i = 1                   # initialize i at 1
    while i <= rows - 1:    # while loop to keep i within bounds of matrix
        tab_table[i][0] = tab_table[i - 1][0] + field[i][0]    # next smallest unsolved subproblem
        i += 1 # increase i by 1

    # filling in the remaining cells
    j = 1
    while j <= cols - 1:  # while loop to keep j within column bounds of matrix
        i = 1
        while i <= rows - 1:      # keep i within row bounds of matrix
            above = tab_table[i - 1][j]  # robot comes from cell above
            left = tab_table[i][j - 1]   # robot comes from cell to the left
            tab_table[i][j] = max(above, left) + field[i][j]   # update tab_table based on max value
            i += 1  # increase i by 1
        j += 1 # increase j by 1

    return tab_table[rows - 1][cols - 1]  # return count in final cell, staying within bounds of matrix

#  <<<<<<< MAIN >>>>>>>

field = []
rows = int(input("\nHow many rows?: "))
cols = int(input("How many columns? "))
if(rows < 1 or cols < 1):
    print("Invalid inputs.  Field must exist in 2D space.")
    quit()

#For using shell to display field
make_field(field, rows, cols)
display(field, cols, "FIELD")

#Make an info_table and get answer using memoization.
info_table = []
make_table(info_table, rows, cols)
ans = max_collect_memo(field, rows-1, cols-1, info_table)
print("\n<<<<< USING MEMOIZATION >>>>>")
display(info_table, cols, "MEMOIZATION TABLE")
print("\nThe most pebbles the robot can collect is ", ans, ".\n")


#Make a tab_table and get answer using tabulation.
tab_table = []
make_table(tab_table, rows, cols)
ans = max_collect_tab(field, rows, cols, tab_table)
print("\n<<<<< USING TABULATION >>>>>")
display(tab_table, cols, "TABULATION TABLE")
print("\nThe most pebbles the robot can collect is ", ans, ".\n")
