class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 1
        n = bin(N)[2:]
        op=''
        for i in range(len(n)):
            if n[i] == '0':
                op+= '1'
            else:
                op+='0'
        return (int(op,2))