class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        totalcost = 0

        # n = -(-len(costs)//2)

        costs = sorted(costs, key=lambda cost: cost[0] - cost[1])

        for i in range(len(costs) // 2):
            totalcost += costs[i][0]
        for i in range(len(costs) // 2, len(costs)):
            totalcost += costs[i][1]

        return totalcost