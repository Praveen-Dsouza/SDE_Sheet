def __init__(self):
    self.arr =[]

def isEmpty(self):
    if self.arr == []:
        return True
    return False

def enqueue(self, x):
    self.arr.append(x)

def dequeue(self): 
    if self.isEmpty(): return -1
    return self.arr.pop(0)

def peek(self):
    if self.isEmpty(): return -1
    return self.arr[0]

def delete(self):
    self.arr = None