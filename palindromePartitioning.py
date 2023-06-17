def partition(self, s):
    result = []
    self.backtrack(s, [], result)
    return result

def backtrack(self, s, path, result):
    if len(s) == 0:
        result.append(path)

    for i in range(len(s)):
        temp = s[:i+1]
        if temp == temp[::-1]: # check Palindrome
            # string to check = s[:i+1] 
            # string remaining = s[i+1:]
            self.backtrack(s[i+1:], path + [temp], result)