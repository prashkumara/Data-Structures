def missingNumbers(arr, brr):

    hashmaparr = collections.Counter(arr)
    hashmapbrr = collections.Counter(brr)


    return list(sorted((hashmapbrr - hashmaparr).keys()))