def myAtoi(s):
    # Remove leading and trailing white spaces
    s = s.strip()
    if not s: return 0
    
    # Check for sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    # Read digits and convert to integer
    num = 0
    for c in s:
        if not c.isdigit():
            # return -1 for gfg
            break
        num = num * 10 + int(c)
    
    # Apply sign and check for overflow
    num = num * sign
    if num < -2**31: return -2**31
    elif num > 2**31 - 1: return 2**31 - 1
    else: return num