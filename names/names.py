import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
from binary_search_tree import BSTNode
duplicates = []
bst = BSTNode(names_1[0])
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name) == True:
        duplicates.append(name)
    else:
        pass
# This runs correctly and gives a runtime of .097 seconds finding the 64 duplicats. 
# Vastly superior to the 6.5s original.
"""

duplicates = list(set(set(names_2) & set(names_1)))  
# This current run time is .003 seconds. 64 duplicates. This is the simpliest way. Stretch goals. 

#duplicates = [i for i, j in zip(names_1, names_2) if i == j]
# this fails, because I think it's comparing point for point rather than the whole list.

"""
The original runtime for my machine was 6.5s finding 64 duplicates.

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
