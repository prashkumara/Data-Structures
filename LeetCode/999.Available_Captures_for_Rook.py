class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for rows in range(8):
            for cols in range(8):
                if board[rows][cols] == "R":
                    row,col = rows,cols

        for i in range(row,8):
            if board[i][col] == 'B':
                break
            if board[i][col] == 'p':
                count+=1
                break

        for i in range(row,-1,-1):
            if board[i][col] == 'B':
                break
            if board[i][col] == 'p':
                count+=1
                break

        for i in range(col,8):
            if board[row][i] == 'B':
                break
            if board[row][i] == 'p':
                count+=1
                break

        for i in range(col,-1,-1):
            if board[row][i] == 'B':
                break
            if board[row][i] == 'p':
                count+=1
                break
        return(count)