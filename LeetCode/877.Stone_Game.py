class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alexCount = 0
        leeCount = 0

        while piles:

            if (piles[0] <= piles[len(piles) - 1]):
                leeCount += piles.pop(0)
            else:
                leeCount += piles.pop(len(piles) - 1)

            if (piles[0] <= piles[len(piles) - 1]):
                alexCount += piles.pop(len(piles) - 1)
            else:
                alexCount += piles.pop(0)

        return alexCount > leeCount