"""
Question 2: Pascal's Triangle
-----------------------------
Difficulty: Easy/Medium

Problem Statement:
Given an integer numRows, return the first numRows of Pascal's triangle. 
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Conceptual Logic
----------------
1. Brute Force (Formulaic):
   * Every element in Pascal's triangle can be calculated using the combination 
     formula nCr, where n is the row index and r is the column index (starting from 0).
   * To build the whole triangle, you would call an nCr function for every single position.

2. Better (Iterative Addition):
   * Instead of complex math, use the property that each number is the sum of 
     the two numbers above it.
   * A row always starts and ends with 1.
   * For the middle elements: row[i] = previousRow[i-1] + previousRow[i].

3. Optimal (Mathematical Optimization):
   * Generating a specific row can be done in O(N) time by observing that each 
     element is (previous_element * (row - col) / col).
   * This allows you to generate each row without needing to store or look up 
     the entire previous row constantly in a separate memory buffer.

Complexity Analysis
-------------------
* Time Complexity: O(numRows^2)
  We are calculating every element in the triangle. There are roughly 
  (numRows * (numRows + 1)) / 2 elements.

* Space Complexity: O(numRows^2)
  To store the result that we need to return. If we ignore the space used for 
  the output, the auxiliary space is O(1) for the optimal iterative method.
"""

"""
PROBLEM: Pascal's Triangle
--------------------------
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

# ==========================================
# APPROACH 1: Brute Force (Using nCr Formula)
# ==========================================
def generate_pascal_brute(numRows):
    """
    Logic: Calculate each element using nCr = n! / (r! * (n-r)!)
    Complexity: Time O(N^3) due to factorial calculations, Space O(N^2)
    """
    def nCr(n, r):
        res = 1
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        return res

    triangle = []
    for row in range(numRows):
        temp_list = []
        for col in range(row + 1):
            temp_list.append(nCr(row, col))
        triangle.append(temp_list)
    return triangle

# ==========================================
# APPROACH 2: Better (Iterative Addition)
# ==========================================
def generate_pascal_better(numRows):
    """
    Logic: Use the sum of the two numbers directly above.
    Complexity: Time O(N^2), Space O(N^2)
    """
    if numRows == 0: return []
    
    triangle = [[1]]
    
    for i in range(1, numRows):
        prev_row = triangle[i-1]
        # Every row starts with 1
        curr_row = [1]
        
        # Calculate middle elements
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
            
        # Every row ends with 1
        curr_row.append(1)
        triangle.append(curr_row)
        
    return triangle

# ==========================================
# APPROACH 3: Optimal (Row Generation Pattern)
# ==========================================
def generate_pascal_optimal(numRows):
    """
    Logic: Generate each row in linear time using the current element to 
    find the next: next_element = prev_element * (row_index - col_index) / col_index
    Complexity: Time O(N^2), Space O(1) (excluding result storage)
    """
    def generateRow(row_num):
        ans = 1
        row = [1]
        for col in range(1, row_num):
            ans = ans * (row_num - col)
            ans = ans // col
            row.append(ans)
        return row

    triangle = []
    for i in range(1, numRows + 1):
        triangle.append(generateRow(i))
    return triangle

# ==========================================
# DRIVER CODE (To Test Functionality)
# ==========================================
if __name__ == "__main__":
    n = 5
    
    print(f"Generating Pascal's Triangle for {n} rows:")
    print("-" * 30)
    
    # Test Brute Force
    print("Brute Force (nCr):")
    print(generate_pascal_brute(n))
    
    # Test Better
    print("\nBetter (Addition):")
    print(generate_pascal_better(n))
    
    # Test Optimal
    print("\nOptimal (Linear Row Gen):")
    print(generate_pascal_optimal(n))
    print("-" * 30)