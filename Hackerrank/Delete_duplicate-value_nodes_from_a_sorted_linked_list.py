def removeDuplicates(head):
    curr_node = head
    next_node = curr_node.next

    while curr_node.next != None:
        flag = 1
        if curr_node.data == next_node.data:
            temp = next_node.next
            next_node = next_node.next
            curr_node.next = temp
            flag = 0
        if flag == 1:
            curr_node = curr_node.next

            if curr_node == None:
                return head
            next_node = curr_node.next
    return head