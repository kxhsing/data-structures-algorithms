def print_recursively(lst):
    """Print items in the list, using recursion."""
    if len(lst) == 0:
        return

    last = lst[0]

    print last 
    print_recursively(lst[1:])
