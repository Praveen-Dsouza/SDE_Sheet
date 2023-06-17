# O(n) time / O(1) space
def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    currSum = 0
    for i in range(len(s)):
        # val < next val
        if (i + 1) < len(s) and roman[s[i]] < roman[s[i+1]]:
            currSum -= roman[s[i]]
        else:
            currSum += roman[s[i]]
    return currSum