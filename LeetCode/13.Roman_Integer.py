class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0

        hashmap = {
                    "I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000
                }

        res = hashmap[s[len(s)-1]]

        for i in range(len(s)-2,-1,-1):
            if hashmap[s[i]]>=hashmap[s[i+1]]:
                res+=hashmap[s[i]]
            else:
                res-=hashmap[s[i]]

        return(res)