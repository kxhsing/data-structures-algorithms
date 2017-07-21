def bubble_sort(lst):
    """For optimal, check if made any swaps, can also keep counter of how many
    swaps were made"""

    swaps_made = 0

    for i in range(len(lst)):
        made_swap = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                made_swap = True
                swaps_made += 1

        if not made_swap:
            break

    return lst #or can return # swaps made if that's what we're looing for