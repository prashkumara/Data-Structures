class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        op = []
        s = list(s)
        for i in s:
            if i in vowels:
                op.append(i)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = op.pop()

        return ("".join(s))