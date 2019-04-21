"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Perform binary search for value in input list."""
    
    # Define helper function
    def split_in_2(a_list):
        """Split list into two"""
        l = len(a_list)
        return a_list[:l/2], a_list[l/2:] # Works whether the list is odd or even

    value_index = 0
    full = input_array

    # Until list has one element
    while len(full) > 1:
        # Split list
        first_half, second_half = split_in_2(full)

        # Keep half that may contain value
        if second_half[0] <= value:
            full = second_half
            # Update value index position
            value_index += len(first_half)
        else:
            full = first_half

    # If remaining element is value, return its index
    if full[0] == value: return value_index
    
    # Else, element isn't in list, return -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)