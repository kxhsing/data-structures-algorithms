"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""

    if len(lst) > 1:
        mid = len(lst)/2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)

        left_i = right_i = new_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                lst[new_i] = left[left_i]
                left_i += 1
            else:
                lst[new_i] = right[right_i]
                right_i += 1
            new_i += 1

        while left_i < len(left):
            lst[new_i] = left[left_i]
            left_i += 1
            new_i += 1

        while right_i < len(right):
            lst[new_i] = right[right_i]
            right_i += 1
            new_i += 1

    # return lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
