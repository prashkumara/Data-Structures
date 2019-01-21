class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        op = ''
        for key,value in count.most_common():
            op += key*value
        return (op)