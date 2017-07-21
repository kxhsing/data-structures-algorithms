#using hash
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    current = head
    seen = set()
    while current:
        if current in seen:
            return True
        else:
            seen.add(current)
        current = current.next
    return False

#no extra space
def hasCycle_2(head):
    turtle = head
    hare = head
    while turtle and hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next
        if turtle == hare:
            return True
    return False