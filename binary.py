##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################

# function getBinaryStrings
# Input n: integer
# constraints: n > 0
# Output: returns a list of binary numbers of length n, in numerical order
#         represent each binary number as a list of n 1s and 0s
#         ex:
#            101 would be [1, 0, 1]
#            0001 would be [0, 0, 0, 1]

# Examples:
# |---------|----------------------------------------------------------|
# |  Input  |                         Output                           |
# |---------|----------------------------------------------------------|
# |    1    | [[0], [1]]                                               |
# |---------|----------------------------------------------------------|
# |    2    | [[0, 0], [0, 1], [1, 0], [1, 1]]                         |
# |---------|----------------------------------------------------------|
# |    4    | [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], |
# |         |  [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], |
# |         |  [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], | 
# |         |  [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]] |
# |---------|----------------------------------------------------------|
def getBinaryStrings(n, i=0, current=None):
    if current is None:
        current = []

    if i == n:
        return [current]

    return getBinaryStrings(n, i + 1, current + [0]) + getBinaryStrings(n, i + 1, current + [1])
##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################
