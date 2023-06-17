# O(s + t) time / O(s + t) space
def isAnagram(s, t):
    if len(s) != len(t): return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        # counting occurrence of each char
        countS[s[i]] = 1 + countS.get(s[i], 0) #get (char, default val if not found)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for ch in countS:
            # we are using .get bcuz if key is not in hashmap of countT it returns 0
        if countS[ch] != countT.get(ch, 0):
            return False
            
    return True

# O(s + t) time / O(s + t) space
def isAnagram(s, t):
    return Counter(s) == Counter(t)

# O(s + t) time / O(1) space
def isAnagram(s, t):
    return sorted(s) == sorted(t)