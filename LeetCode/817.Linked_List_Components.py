def numComponents(self, head, G):
    """
    :type head: ListNode
    :type G: List[int]
    :rtype: int
    """
    G = set(G)
    curr = head
    flag = True
    op = 0
    while curr:
        if curr.val in G:
            if flag:
                op += 1
                flag = False
        else:
            flag = True
        curr = curr.next
    return op