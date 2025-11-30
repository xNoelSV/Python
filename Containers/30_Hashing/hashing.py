"""
This module shows how Python's built-in hash() function works with tuples,
which are hashable (immutable) data structures. The hash() function computes
a hash value for an object, which is used internally for dictionary keys and
set members. Tuples, being immutable, are hashable and can be safely hashed,
unlike lists which are mutable and cannot be hashed.

Note: Hash values are implementation-dependent and may vary between Python
interpreter runs when hash randomization is enabled.
"""

print(hash((1, 2, 3)))
print(hash((1, 2, [])))