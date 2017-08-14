def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head:
        while head.val == val:
            head = head.next
            if head is None:
                return []

        current = head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next

        return head