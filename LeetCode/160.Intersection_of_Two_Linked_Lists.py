def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA == None or headB == None:
        return None

    curr1, curr2 = headA, headB

    while curr1 != curr2:
        if curr1 == None:
            curr1 = headB
        else:
            curr1 = curr1.next

        if curr2 == None:
            curr2 = headA
        else:
            curr2 = curr2.next
    return curr1