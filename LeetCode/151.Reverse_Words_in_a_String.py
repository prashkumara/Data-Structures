class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split(" ")
        while '' in s:
            s.remove('');
        return " ".join(s[::-1])