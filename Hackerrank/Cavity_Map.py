def cavityMap(grid):
    grid1=[]
    for i in range(1,len(grid)-1):
        str1=''
        for j in range(1,len(grid)-1):
            if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                grid[i][j]='X'
    for i in grid:
        grid1.append(''.join(i))
    return grid1