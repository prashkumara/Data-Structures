def matchingStrings(strings, queries):
    stringMap = {}
    lis = []
    for string in strings:
        if string not in stringMap:
            stringMap.update({string: 1})
        else:
            stringMap.update({string: stringMap[string] + 1})

    for query in queries:
        if query in stringMap:
            lis.append(stringMap[query])
        else:
            lis.append(0)
    return lis