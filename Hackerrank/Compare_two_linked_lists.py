def compare_lists(llist1, llist2):
    curr1 = llist1
    curr2 = llist2

    if curr1 == None and curr2 != None:
        return 0
    if curr2 == None and curr1 != None:
        return 0
    if curr1 == None and curr2 == None:
        return 1

    while curr1 != None and curr2 != None:
        if curr1.data != curr2.data:
            return 0
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 != None:
        return 0
    if curr2 != None:
        return 0

    return 1