def hourglassSum(arr):
    sumArr = -999
    if len(arr) == 0 or len(arr) == 1:
        return arr
    for i in range(1, len(arr) - 1):

        for j in range(1, len(arr[0]) - 1):
            sum1 = 0
            sum1 = arr[i][j] + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i + 1][j - 1] + arr[i + 1][
                j] + arr[i + 1][j + 1]

            if sum1 > sumArr:
                sumArr = sum1

    return sumArr