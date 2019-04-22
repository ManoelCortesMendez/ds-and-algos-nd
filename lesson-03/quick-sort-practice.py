"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    """Sort array using quicksort"""

    # Define base case
    if len(array) <= 1: return array
    
    # Get pivot value
    pivot = array[-1]

    # Initialze lists to store results
    before_pivot = []
    after_pivot = []

    # Distribute values according to whether they're...
    for value in array[:-1]:
        if value < pivot: # ... smaller than the pivot
            before_pivot.append(value)
        else: # ... greater than the pivot
            after_pivot.append(value)

    # Recurse
    return quicksort(before_pivot) + [pivot] + quicksort(after_pivot)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)