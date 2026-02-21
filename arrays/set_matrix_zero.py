import copy  # Imported to create deep copies for testing different approaches

"""
PROBLEM: Set Matrix Zeroes
--------------------------
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.
You must do this in-place (without creating a new full-sized matrix).

Link: Striver's SDE Sheet - Arrays Part 1
"""

# ==========================================
# APPROACH 1: Brute Force
# ==========================================
def setZeroes_Brute(matrix):
    """
    Approach 1: Brute Force (Marking with -1)
    -----------------------------------------
    Visual Intuition:
    Imagine checking a checklist. If you find a "failure" (0), you don't want to 
    cross out the whole row *immediately* because you might confuse a "crossed out" 
    box with a real failure later. Instead, you mark it with a temporary symbol (like -1).
    Once you've checked the whole list, you go back and turn all -1s into real 0s.

    Steps:
    1. Iterate through the matrix.
    2. If you find matrix[i][j] == 0, iterate through its specific row and column 
       and mark all non-zero cells as -1.
    3. Iterate through the matrix again and change all -1s to 0.

    Complexity:
    - Time: O((N*M) * (N + M)) -> Very slow (near cubic).
    - Space: O(1) -> In-place.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Mark rows and columns with -1 (if they are not already 0)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                # Mark entire Row i
                for k in range(cols):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                # Mark entire Column j
                for k in range(rows):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1

    # Step 2: Convert -1 back to 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# ==========================================
# APPROACH 2: Better Solution
# ==========================================
def setZeroes_Better(matrix):
    """
    Approach 2: Better (Row & Col Arrays)
    -------------------------------------
    Visual Intuition:
    Instead of writing on the main sheet, keep two small notepads: one for Rows 
    and one for Columns. If you see a 0 at (2, 3), put a checkmark on 
    Row Notepad #2 and Col Notepad #3. After checking every cell, just look at 
    your notepads. If Row 2 has a checkmark, turn the whole row to 0.

    Steps:
    1. Create two dummy arrays: row_dummy (size N) and col_dummy (size M).
    2. Traverse matrix. If matrix[i][j] == 0, mark row_dummy[i] = 1 and col_dummy[j] = 1.
    3. Traverse matrix again. If row_dummy[i] or col_dummy[j] is 1, set cell to 0.

    Complexity:
    - Time: O(2 * N * M) -> Two passes.
    - Space: O(N + M) -> Extra space for dummy arrays.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create two separate arrays to track zeroes
    row_dummy = [0] * rows
    col_dummy = [0] * cols
    
    # Step 1: Traverse and mark the dummy arrays
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_dummy[i] = 1
                col_dummy[j] = 1
                
    # Step 2: Update matrix based on dummy arrays
    for i in range(rows):
        for j in range(cols):
            if row_dummy[i] == 1 or col_dummy[j] == 1:
                matrix[i][j] = 0

# ==========================================
# APPROACH 3: Optimal Solution
# ==========================================
def setZeroes_Optimal(matrix):
    """
    Approach 3: Optimal (In-Place / Markers)
    ----------------------------------------
    Visual Intuition:
    We don't want to use extra space O(N+M), so we use the First Row and 
    First Column of the matrix *as* our notepads.
    
    The Problem: matrix[0][0] overlaps. It belongs to both Row 0 and Col 0.
    The Fix: Use matrix[0][0] for Row 0's status, and a separate variable 'col0' 
    for Column 0's status.

    Steps:
    1. Traverse matrix. If matrix[i][j] == 0:
       - Mark top of column: matrix[0][j] = 0
       - Mark left of row: matrix[i][0] = 0
       - (Handle col0 separately if j == 0)
    2. Traverse inner matrix (1 to N, 1 to M) and fill 0s based on markers.
    3. Update the First Row and First Column last to avoid polluting markers early.

    Complexity:
    - Time: O(2 * N * M)
    - Space: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1  # The "sticky note" for the first column
    
    # Step 1: Traverse and mark the first row/col
    for i in range(rows):
        # Check if the 0 is in the first column
        if matrix[i][0] == 0:
            col0 = 0
        
        # Check the rest of the row
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row i
                matrix[0][j] = 0  # Mark col j
    
    # Step 2: Update the inner matrix (from 1,1)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Step 3: Handle the First Row
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0
            
    # Step 4: Handle the First Column
    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

# ==========================================
# DRIVER CODE (To Test Functionality)
# ==========================================
if __name__ == "__main__":
    # Test Case
    original_matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print("Original Matrix:")
    for row in original_matrix:
        print(row)
    print("-" * 20)

    # Test Brute Force
    print("Testing Brute Force:")
    mat1 = copy.deepcopy(original_matrix)
    setZeroes_Brute(mat1)
    for row in mat1: print(row)
    print("-" * 20)

    # Test Better Approach
    print("Testing Better Approach:")
    mat2 = copy.deepcopy(original_matrix)
    setZeroes_Better(mat2)
    for row in mat2: print(row)
    print("-" * 20)

    # Test Optimal Approach
    print("Testing Optimal Approach:")
    mat3 = copy.deepcopy(original_matrix)
    setZeroes_Optimal(mat3)
    for row in mat3: print(row)