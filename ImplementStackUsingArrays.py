def __init__(self):
    self.arr=[]
    
def isEmpty(self):
    if self.arr == []:
        return True
    return False

def push(self,data):
    self.arr.append(data)

def pop(self):
    if self.isEmpty(): 
        return -1
    return self.arr.pop()

def peek(self):
    if self.isEmpty():
        return -1
    return self.arr[len(self.arr)-1]

def delete(self):
    self.arr = None