import numpy as np


def done_or_not(board):
    my_array = np.array(board)

    count = 0

    # First check if columns and rows contains numbers 1 through 9.
    for number in range(9):
        if len(set(my_array[number])) == 9 and len(set(my_array[:, number])) == 9:
            count += 1

    # If our columns and rows don't contain numbers 1 through 9 then no need to continue the function.
    if count != 9:
        return "Try again!"

    # Next check if the cube sections also contain numbers 1 through 9.
    for outer_number in [0, 3, 6]:
        for inner_number in [0, 3, 6]:
            if len(set(my_array[outer_number:outer_number +
                                3, inner_number:inner_number + 3].flatten())) == 9:
                count += 1

    if count == 18:
        return "Finished!"
    else:
        return "Try again!"


print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [
      5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 5, 3]]))
