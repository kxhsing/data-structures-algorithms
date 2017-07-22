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


