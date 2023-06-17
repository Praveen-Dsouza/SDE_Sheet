# O(n) time / O(n) space
def sorted(self, s):
    self.reverse(s)
    
def reverse(self, s):
    if s:
        val = s[-1]
        s.pop()
        self.reverse(s)
        self.insertCorrectPosition(val, s)
        
def insertCorrectPosition(self, val, s):
    if not s or s[-1] < val:
        s.append(val)
    else:
        top = s[-1]
        s.pop()
        self.insertCorrectPosition(val, s)
        s.append(top)