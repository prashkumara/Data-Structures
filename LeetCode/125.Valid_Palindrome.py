class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        res = []
        s=s.lower()
        for i in s:
            if i.isalnum():
                res.append(i)
        return res==res[::-1]