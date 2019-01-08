def leftRotation(arr, n, d):
    print(' '.join(str(s) for s in (arr[d:] + arr[0:d])))