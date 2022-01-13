# Python3 program to illustrate
# Saddle point

# Method to find saddle point
def findSaddlePoint(mat, n):

    # Process all rows one
    # by one
    for i in range(n):

        # Find the minimum element
        # of row i.
        # Also find column index of
        # the minimum element
        min_row = mat[i][0]
        col_ind = 0
        for j in range(1, n):
            if (min_row > mat[i][j]):
                min_row = mat[i][j]
                col_ind = j

        # Check if the minimum element
        # of row is also the maximum
        # element of column or not
        k = 0
        for k in range(n):

            # Note that col_ind is fixed
            if (min_row < mat[k][col_ind]):
                break
            k += 1

        # If saddle point present in this
        # row then print
        if (k == n):
            print("Value of Saddle Point ",
                  min_row)
            return True

    # If Saddle Point found
    return False


# Driver method
if __name__ == '__main__':

    mat = [[1, 2, 3],
           [4, 5, 6],
           [8, 9, 10]]

    n = 3
    if (findSaddlePoint(mat, n) ==
            False):
        print("No Saddle Po")
