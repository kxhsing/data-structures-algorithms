def find_needle(lst, target):
    """Find the target ("needle") in the list ("haystack") using recursion.
    Return its index in the list. Return None if not found."""

    def helper(lst, target):
        if lst is None:
            raise ValueError

        if lst[0] == target:
            return 0

        return helper(lst[1:], target) + 1

    try:
        helper(lst, target)

    except ValueError:
        return None

