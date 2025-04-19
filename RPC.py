# pop function
def pop(stk, sp):
    val = stk[sp[0]]
    sp[0] = sp[0] - 1   # move stack pointer
    return val          # return value

# push function
def push(val, stk, sp):
    sp[0] = sp[0] + 1        # move stack pointer
    if sp[0] == len(stk):
        stk.append(val)       # append stack
    else:
        stk[sp[0]] = val

def calculate(str, k):
    # initialize variables
    stk = []
    sp = [-1]
    k = 0

    while k < len(str):   # while loop for reverse polish calculation
        val = str[k]

        if type(val) == float:    # conditional if val is a float
            push(val, stk, sp)    # call push function
        elif val == "+":          # conditional for val is addition
            if sp[0] >= 1:
                x = pop(stk, sp)     # if conditions are met, call pop function
                y = pop(stk, sp)
                push(x + y, stk, sp)  # push result onto stack
        elif val == "-":             # conditional for if val is subtraction
            if sp[0] >= 1:
                x = pop(stk, sp)      # if conditions are met, call pop function
                y = pop(stk, sp)
                push(y - x, stk, sp)   # push result onto stack
        elif val == "x":                # conditional if val is multiplication
            if sp[0] >= 1:
                x = pop(stk, sp)       # if conditions are met, call pop function
                y = pop(stk, sp)
                push(x * y, stk, sp)   # push result onto stack
        elif val == "/":              # conditional for is val is division
            if sp[0] >= 1:
                x = pop(stk, sp)       # if conditions are met, call pop function
                y = pop(stk, sp)
                push(y / x, stk, sp)    #push result onto stack
        k += 1                         # increment by 1

    return stk[0]                  # return final result

# converting string types  function
def convert_str_types(str):
    k = 0                          # initialize variable k
    while k < len(str):          # start while loop
        char = ord(str[k][0])
        if char >= 48 and char <= 57: # conditional for ascii values (checking to see if it between 0 and 9)
            str[k] = float(str[k])     # turn string value at 'k' into float if conditional is true
        k += 1                       # increment by 1

################# MAIN CALLING ROUTINE ################
from sys import *
# initialize empty list and k
str = []
k = 1
while k < len(argv):      # while loop
    str.append(argv[k])
    k = k + 1
print(str)          # print inputs

convert_str_types(str) # call convert function
ans = calculate(str, k)    # assign return value from calculate function to ans
print(ans)       # print ans
