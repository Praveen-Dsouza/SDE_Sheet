def __init__(self):
    self.input = []
    self.output = []

def push(self, x):
    return self.input.append(x)

def pop(self):
    self.move()
    return self.output.pop()

def peek(self):
    self.move()
    return self.output[-1]

def empty(self):
    if self.input == [] and self.output == []: return True
    return False

def move(self):
    if not self.output:
        while self.input:
            self.output.append(self.input.pop())