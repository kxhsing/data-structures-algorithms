def merge_sorted_ll(l1, l2):
    """Given two sorted linked lists, merge"""

    # create dummy node with data of 0 to start
    new_dummy_head = current = Node(0) 

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next

        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    # if we run out of node in a list, set the rest of it to the list with nodes left
    current.next = l1 or l2 

    return new_dummy_head.next



