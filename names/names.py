import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# The old code is an O(n^2) function it ran in 9 seconds on my local machine
# the old code appended 64 duplicates.


 # We can use a binary search tree to look for values
# First, create a BST (put first element as the root)           
bst = BSTNode(names_1[0])
# add all the names from names_1 in the tree
for name in names_1[1:]: # Insert remaining nodes from names_1
    bst.insert(name)

# for each name in the second list
# check if the name is in the tree
# if True, add the name to the duplicate list
for name in names_2: # Checking if my bst contains a name in names_2
    if bst.contains(name):
        duplicates.append(name)
# The new code is O(n log n) it takes 0.9 seconds on my local machine
# the new code appended 64 duplicates. 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
# runtime dropped from 9s to 0.13s

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
