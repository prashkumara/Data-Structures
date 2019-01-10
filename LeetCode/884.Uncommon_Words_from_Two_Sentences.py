class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        str1 = A.split(" ")
        str2 = B.split(" ")
        hashmap = {}
        lis = []
        for w in str1:
            if w not in hashmap:
                hashmap.update({w: 1})
            else:
                hashmap.update({w: hashmap[w] + 1})

        for w in str2:
            if w not in hashmap:
                hashmap.update({w: 1})
            else:
                hashmap.update({w: hashmap[w] + 1})

        for key in hashmap:
            if hashmap[key] == 1:
                lis.append(key)
        return lis