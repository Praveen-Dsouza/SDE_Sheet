def reverseWords(s):
    i, j = 0, len(s)-1
    n, res = len(s), ''
    while i < n:
        # Increment i until non space
        while i < n and s[i] == ' ':
            i += 1
        if i >= n: break
        j = i + 1
        # Increment j till space
        while j < n and s[j] != ' ':
            j += 1
        word = s[i : j] # word before ' '
        # append the word 
        if len(res) == 0:
            res = word
        else:
            res = word + ' ' + res
        i = j + 1
    return res