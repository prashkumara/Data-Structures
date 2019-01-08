class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.rstrip().split(" ")

        if len(words)<1:
            return 0
        return len(words[len(words)-1])