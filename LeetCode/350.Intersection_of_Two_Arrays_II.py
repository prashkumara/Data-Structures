def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    hashmap1 = {}
    hashmap2 = {}
    for n in nums1:
        if n not in hashmap1:
            hashmap1.update({n: 1})
        else:
            hashmap1.update({n: hashmap1[n] + 1})
    for n in nums2:
        if n not in hashmap2:
            hashmap2.update({n: 1})
        else:
            hashmap2.update({n: hashmap2[n] + 1})
    resultmap = {}
    lis = []
    for k in hashmap1:
        if k in hashmap2:
            if hashmap1[k] < hashmap2[k]:
                resultmap.update({k: hashmap1[k]})
            else:
                resultmap.update({k: hashmap2[k]})
    for k in resultmap:
        for i in range(resultmap[k]):
            lis.append(k)
    return lis