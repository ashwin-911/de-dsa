"""
PROBLEM: Linear Search
----------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an array 'arr' and an integer 'target', find the index of the first occurrence 
of 'target' in the array. If the target is not found, return -1.

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Standard Iterative Approach:
   - Logic: 
     Since the array is NOT sorted, we have no clues about where the number might be.
     We have to check every single element one by one from the start.
   - Analogy: 
     Searching for a specific book on a messy, unorganized bookshelf. 
     You have to pick up the first book, check the title. If it's not the one, 
     you pick up the second, and so on. You can't skip any books because the 
     one you want might be hiding right there.

2. Recursive Approach (For concept):
   - Logic: 
     Check the first element. If it matches, great! 
     If not, delegate the search to the rest of the array (index+1 onwards).
   - Analogy: 
     You ask the first person in line, "Are you Bob?". If no, you tell them 
     to ask the person behind them.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Time Complexity: O(N)
   - Worst Case: The element is at the very end or not present at all. 
     We have to check N elements.
   - Best Case: The element is at index 0 (O(1)).

2. Space Complexity: O(1)
   - We only use a loop variable. (Recursive approach would take O(N) stack space).
"""

# ==========================================
# APPROACH 1: Standard Iterative (Optimal)
# ==========================================
def linearSearch_Iterative(arr, target):
    """
    Approach 1: Standard Iterative
    ------------------------------
    Visual Intuition:
    The "Scanner" method. A pointer moves from Left to Right.
    It stops the moment it finds a match.

    Steps:
    1. Iterate loop 'i' from 0 to N-1.
    2. At each step, check if arr[i] == target.
    3. If yes, return i.
    4. If loop finishes without finding match, return -1.

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
            
    return -1

# ==========================================
# APPROACH 2: Recursive (For Practice)
# ==========================================
def linearSearch_Recursive(arr, target, index=0):
    """
    Approach 2: Recursive
    ---------------------
    Visual Intuition:
    Passing the baton. 
    "Is it me? No? Okay, next person check yourself."

    Steps:
    1. Base Case 1: If index == len(arr), we reached end -> return -1.
    2. Base Case 2: If arr[index] == target -> return index.
    3. Recursive Step: Return result of searching (index + 1).

    Complexity:
    - Time: O(N)
    - Space: O(N) (Recursion Stack) - Not efficient for production.
    """
    # Base Case: Reached end of array without finding it
    if index >= len(arr):
        return -1
        
    # Base Case: Found the target
    if arr[index] == target:
        return index
        
    # Recursive Call
    return linearSearch_Recursive(arr, target, index + 1)

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Target Exists
    arr1 = [1, 2, 3, 4, 5]
    target1 = 4
    print(f"Array: {arr1}, Target: {target1}")
    print(f"Iterative Result (Index): {linearSearch_Iterative(arr1, target1)}")
    
    # Test Case 2: Target Does Not Exist
    arr2 = [10, 20, 30]
    target2 = 99
    print(f"\nArray: {arr2}, Target: {target2}")
    print(f"Iterative Result (Index): {linearSearch_Iterative(arr2, target2)}")
    
    # Test Case 3: Multiple Occurrences (Should return first)
    arr3 = [1, 2, 3, 2, 1]
    target3 = 2
    print(f"\nArray: {arr3}, Target: {target3}")
    # Should return index 1, not 3
    print(f"Recursive Result (Index): {linearSearch_Recursive(arr3, target3)}")