def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    lis1 = []
    lis2 = []
    curr1 = l1
    curr2 = l2

    sum1 = 0
    sum2 = 0

    while curr1 != None:
        lis1.append(curr1.val)
        curr1 = curr1.next

    while curr2 != None:
        lis2.append(curr2.val)
        curr2 = curr2.next
    print(lis1, lis2)
    po = 0
    for i in range(len(lis1)):
        sum1 = sum1 + lis1[i] * (10 ** po)
        po += 1
    po = 0
    for i in range(len(lis2)):
        sum2 = sum2 + lis2[i] * (10 ** po)
        po += 1

    totalsum = str(sum1 + sum2)
    print(lis1, sum1, lis2, sum2)
    lis3 = [int(i) for i in str(totalsum)]

    finalroot = None

    for i in range(len(lis3) - 1, -1, -1):

        new_node = ListNode(lis3[i])
        curr = finalroot
        if finalroot == None:
            finalroot = new_node

        else:
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
    return finalroot
