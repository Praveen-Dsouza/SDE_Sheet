from collections import defaultdict

# O(n ^ 3) time / O(1) space
def lengthOfLongestSubstring(s):   
    n, res = len(s), 0

    for i in range(n):
        for j in range(i, n):
            if areDistinct(s, i, j):
                res = max(res, j - i + 1)

    return res
    
def areDistinct(s, i, j):
    # if not s or s == " " : return 0

    visited = [0] * 26 #default value is False of visited

    for k in range(i, j + 1):
        if visited[ord(s[k]) - ord('a')] == True:
            return False
        visited[ord(s[k]) - ord('a')] = True

    return True

# O(n ^ 2) time / O(1) space
def lengthOfLongestSubstring(s):
    n, res = len(s), 0

    for i in range(n):
        visited = [0] * 256  #default value is False of visited

        for j in range(i, n):
            # If current character is visited break
            if visited[ord(s[j])] == True: break

            # update window if this window is larger, 
            # and mark current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(s[j])] = True

        # Remove the first character of previous window
        visited[ord(s[i])] = False

    return res

# O(2n) time / O(n) space
def lengthOfLongestSubstring(s):
    maxLen = left = 0
    freqChar = set()
    
    for r in range(len(s)):
        while s[r] in freqChar:
            freqChar.remove(s[left])
            left += 1
        freqChar.add(s[r])
        maxLen = max(r - left + 1, maxLen)
    
    return maxLen

# O(n) time / O(n) space
def lengthOfLongestSubstring(s):
    maxLen = left = 0
    freqChar, n = {}, len(s)

    for right in range(n):
        # Check if already element present or not im map
        if s[right] in freqChar:
            # If present, move the left pointer
            # to position after the last occurrence
            left = max(left, freqChar[s[right]] + 1)
  
        # Updating the last index of the character
        freqChar[s[right]] = right
        maxLen = max(right - left + 1, maxLen)
    return maxLen

