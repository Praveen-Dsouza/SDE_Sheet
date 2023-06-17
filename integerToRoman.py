# O(n) time / O(1) space
def intToRoman(num):
    symList = [ ['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90],
                ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000] ]

    res = ''
    for sym, val in reversed(symList):
        if num // val: # sym val > 0 append in res
            count = num // val # sym count char append in res
            res += (sym * count)
            num = num % val # rem val
    return res