class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {}
        order = []
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
                order.append(i)
            else:
                hashmap[i] = hashmap[i] + 1

        for i in order:
            if hashmap[i] == 1:
                return s.index(i)
        return -1

