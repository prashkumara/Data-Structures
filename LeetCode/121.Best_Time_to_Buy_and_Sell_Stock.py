class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit