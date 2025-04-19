def sort(data, start, end):
    if start >= end:         # base case for empty list or list with only one element
        return [data[start]]

    split = (start + end)//2          # split list operation
    left = sort(data, start, split)    # recursive call to left
    right = sort(data, split + 1, end)    # recursive call to right

    return merge(left, right)      # return statement

def merge(left, right):
    sorted_data = []            # empty list
    lp = 0                      # left pointer
    rp = 0                     # right pointer

    while lp < len(left) and rp < len(right):   # while loop for merging left and right
        if left[lp] < right[rp]:               # compare left list at left pointer with right list at right pointer
            sorted_data.append(left[lp])       # append sorted list if condition evaluates to true (merge)
            lp += 1                          # increment left pointer
        else:
            sorted_data.append(right[rp])     # append sorted list if condition evaluates to false (merge)
            rp += 1                           # increment right pointer

    while lp < len(left):               # while loop for merging left
        sorted_data.append(left[lp])    # merge 
        lp += 1                       # increment

    while rp < len(right):              # while loop for merging right
        sorted_data.append(right[rp])   # merch 
        rp += 1                        #increment
    return sorted_data           # return sorted data




#### MAIN CALLING ROUTINE ###

data = []   # empty list for input data
item = int(input("Enter Data: \n"))

while item != -1:
    data.append(item)
    item = int(input())

start = 0   # initializing start and end
end = len(data) -1

sorted_data = sort(data, start, end)   # sort function call
print(f"Input Data:{data}\nSorted Data: {sorted_data}")   # print input list and sorted list


