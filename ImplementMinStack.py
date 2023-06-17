# O(1) time / O(n) space
def __init__(self):
    self.stack = []
    self.min = float('inf')

def push(self, val):
    value = val
    if not self.stack:
        self.min = value
        self.stack.append(value)
    else:
        if value < self.min:
            self.stack.append(2 * value - self.min)
            self.min = value
        else:
            self.stack.append(value)

def pop(self):
    if not self.stack: return
    el = self.stack[-1]
    self.stack.pop()

    if el < self.min: self.min = 2 * self.min - el # modified value

def top(self):
    if not self.stack: return -1
    el = self.stack[-1]
    if el < self.min: return self.min # if modified value
    return el

def getMin(self):
    return self.min

# O(1) time / O(2n) space
def __init__(self):
    self.stack = []
    self.minStack = []

def push(self, val):
    self.stack.append(val)
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

def pop(self):
    self.stack.pop()
    self.minStack.pop()

def top(self):
    return self.stack[-1]

def getMin(self):
    return self.minStack[-1]