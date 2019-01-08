class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5:
                hashmap.update({i: hashmap[i] + 1})

            elif i == 10:
                hashmap.update({i: hashmap[i] + 1})
                if hashmap[5] > 0:
                    hashmap[5] = hashmap[5] - 1
                else:
                    return False

            elif i == 20:
                hashmap.update({i: hashmap[i] + 1})
                if hashmap[5] > 0 and hashmap[10] > 0:
                    hashmap[5] = hashmap[5] - 1
                    hashmap[10] = hashmap[10] - 1
                elif hashmap[5] > 2:
                    hashmap[5] = hashmap[5] - 3
                else:
                    return False

        return True
