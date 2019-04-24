class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        lis = []
        index=0
        hashmap={}
        for i in range(R):
            for j in range(C):
                hashmap[index] = abs(i-r0) + abs(j-c0)
                index+=1
                lis.append([i,j])

        sortedlist = sorted(hashmap, key=lambda x:hashmap[x])
        outputlist = []
        for i in range(len(sortedlist)):
            outputlist.append(lis[sortedlist[i]])

        return(outputlist)