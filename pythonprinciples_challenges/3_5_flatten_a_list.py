# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling:

# flatten([[1, 2], [3, 4]])
# Should return the list:

# [1, 2, 3, 4]

# Method 1: List Comprehension
def flatten(listOfLists):
    return [x for l in listOfLists for x in l]

## por cada l (elemento de listOfLists) y por cada x in l, colocar x 
## se mete a los elementos de los elementos de las listas

print(flatten([[1, 2], [3, 4]]))

##############################################################################################
##############################################################################################
###############################   S  O  L  U  T  I  O  N  S  #################################
##############################################################################################
##############################################################################################
# Method 2: Unpacking
def flatten(listOfLists):
    return  [*listOfLists[0], *listOfLists[1]]

flatten()

# Method 3: Extend Method
def flatten(listOfLists):
    flat_3 = []
    for l in listOfLists:
        flat_3.extend(l)