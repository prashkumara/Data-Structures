def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr = head

    if curr == None:
        return head

    while curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head