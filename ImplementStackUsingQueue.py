def __init__(self):
    self.queue = []

def push(self, x):
    return self.queue.append(x)

def pop(self): # O(n)
    if self.empty(): return -1
    for i in range(len(self.queue)-1):
        self.push(self.queue.pop(0))
    return self.queue.pop(0)

def top(self):
    return self.queue[-1]

def empty(self):
    if self.queue == []: return True
    return False