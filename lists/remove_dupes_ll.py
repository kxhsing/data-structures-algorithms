def remove_duplicates(head):
    """Given LL, remove duplicates"""
    current = head
    seen = set()

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.data)
            current = current.next


def remove_duplicates_sorted(head):
    """Given a sorted LL, remove duplicates"""

    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next


def remove_k_from_ll(head, k):
    """Remove all k in linked list. There might be duplicates"""

    if l is None:
        return
    
    while l and l.value == k:
        l=l.next
        if l is None:
            return
    
    current = l
    while current.next:
        if current.next.value == k:
            current.next = current.next.next
            if current.next is None:
                return l
        else:
            current = current.next
    return l

