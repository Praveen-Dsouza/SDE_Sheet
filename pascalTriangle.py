def generate(numRows):
    res = [[1]]
    
    for i in range(numRows - 1): #bcuz we already have a row
        temp = [0] + res[-1] + [0] # not modify, create new list
        row = [] # store next row
        for j in range(len(res[-1]) + 1): # len prev row + 1
            row.append(temp[j] + temp[j + 1]) # add two val
        res.append(row)
    return res