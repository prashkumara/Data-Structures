def alternatingCharacters(s):
    res = 0
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            res+=1
    return res