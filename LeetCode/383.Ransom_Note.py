import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomcounter = collections.Counter(ransomNote)
        magazinecounter = collections.Counter(magazine)

        for key in ransomcounter:
            if ransomcounter[key]>magazinecounter[key] or key not in magazinecounter:
                return False
        return True