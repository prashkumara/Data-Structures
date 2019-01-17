class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.hashmap[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sumOp = 0
        for key in self.hashmap:
            if key[:len(prefix)] == prefix:
                sumOp += self.hashmap[key]
        return sumOp

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)