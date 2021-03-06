"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        # If position == 1, return head
        if position == 1:
            return self.head
        
        # Get head
        current = self.head

        # Traverse list until position
        for _ in range(1, position):
            # As long as there are elements, keep going until position
            if current.next:
                current = current.next
            else:
                # If element along the way is empty, or position is outside of list, return None
                return None
        else:
            # If for loop completes, we've reached element at position, so return it
            return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        # If position is 1, we insert a new head
        if position == 1:
            
            # Link new element to current head
            new_element.next = self.head

            # Set new element as new head
            self.head = new_element

        # Get elements that'll come before and after new element
        el_before = self.get_position(position-1)
        el_after = self.get_position(position)

        # Link before element to new element and new element to after element
        el_before.next = new_element
        new_element.next = el_after
    
    def delete(self, value):
        """Delete the first node with a given value."""
        
        # If head value matches...
        if self.head.value == value:
            # ... make second element the new head
            self.head = self.head.next
        
        # Get head
        current = self.head

        # While current element has a next element
        while current.next:
            # If value of next element matches...
            if current.next.value == value:
                # Link current element to element two spots down the chain
                # That is, we skip the element that matches, effectively removing it from the linked list
                current.next = current.next.next
            else:
                # Else, move to next element in list
                current = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value