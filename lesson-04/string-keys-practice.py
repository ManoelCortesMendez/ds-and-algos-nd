"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""

        # Compute string hash to get index
        index = self.calculate_hash_value(string)

        # If a list is stored at index...
        if self.table[index]:
            self.table[index].append(string) # ...append string to list
        else:
            self.table[index] = [string] # Else, store new list with string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""

        # Compute string hash to get index
        index = self.calculate_hash_value(string)

        # If list stored at index
        if self.table[index]:
            # If string is in said list
            if string in self.table[index]:
                return index # Then, return said index

        return -1 # Else, return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        
        # Return hash of string using specific formula
        return ord(string[0]) * 100 + ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
