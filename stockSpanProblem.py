# O(n^2) time / O(n) space
def __init__(self):
    self.stack = []

def next(self, price):
    idx = -1
    for i in range(len(self.stack)-1, -1, -1):
        if self.stack[i] > price: 
            idx = i
            break
    self.stack.append(price)
    return len(self.stack) - idx - 1

# O(n) time / O(n) space
def __init__(self):
    self.stack = [] #pair [stock, span]

def next(self, price):
    span = 1
    while self.stack and self.stack[-1][0] <= price:
        span += self.stack[-1][1]
        self.stack.pop()
    self.stack.append([price, span])
    return self.stack[-1][1]

# GFG 
def calculateSpan(price, n):
    stack = [0 for i in range(n)]
    stack[0] = 1
    for i in range(1, n):
        stack[i] = 1
        j = i-1
        while j >= 0 and price[i] >= price[j]:
            stack[i] += 1
            j -= 1
    return stack
        
    
# O(n) time / O(n) space
def calculateSpan(price, n):
    stack = []
    span = [1 for i in range(n)]
    stack.append(0)
    for i in range(1, n):
        currPrice = price[i]
        while len(stack) and price[stack[-1]] <= currPrice:
            stack.pop()
        if len(stack) == 0:
            span[i] = i+1
        else:
            span[i] = i-stack[-1]
        stack.append(i)
    return span