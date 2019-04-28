import collections


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counter = collections.Counter(deck)

        X = min(counter.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in counter.values()):
                return True
        return False
