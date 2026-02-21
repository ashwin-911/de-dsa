"""
PROBLEM: Check if the Array is Sorted
-------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an array of size N, return True if the array is sorted in non-decreasing order, 
otherwise return False.

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: For every element, check all elements to its right. 
     If we find any element on the right that is smaller than the current element, 
     the array is NOT sorted.
   - Analogy: To ensure everyone in a line is arranged by height, you pick the 
     first person and walk down the line to check if anyone shorter is standing behind them.
     Then you go back, pick the second person, and do it again.

2. Recursive Approach (Divide & Conquer):
   - Logic: Check the first pair. If they are okay, trust the recursion to check 
     the rest of the array.
   - Analogy: You check if you are shorter than the person behind you. If yes, 
     you ask the person behind you to check with the person behind them.

3. Optimal Approach (Single Pass):
   - Logic: We don't need to check everyone against everyone. We only need to 
     check if the current person is taller (or equal) to the immediate previous person.
     If this condition holds for every adjacent pair, the whole array is sorted.
   - Analogy: Just look at your neighbor. If arr[i] >= arr[i-1] for all steps, 
     we are good.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2) -> Two nested loops.
   - Space: O(1)

2. Recursive Approach:
   - Time: O(N) -> N recursive calls.
   - Space: O(N) -> Stack space for recursion.

3. Optimal Approach:
   - Time: O(N) -> Single pass.
   - Space: O(1) -> No extra space.
"""

# ==========================================
# APPROACH 1: Brute Force (Compare All Pairs)
# ==========================================
def isSorted_Brute(arr):
    """
    Approach 1: Brute Force (Nested Loops)
    --------------------------------------
    Visual Intuition:
    Imagine checking a stack of papers. You pick the top paper (Index i) and 
    compare it with EVERY paper below it (Index j). If you find any paper below 
    that should have been on top (arr[j] < arr[i]), the stack is messed up.

    Steps:
    1. Iterate loop 'i' from 0 to N-1.
    2. Iterate loop 'j' from i+1 to N.
    3. If arr[j] < arr[i], return False immediately.
    4. If loops finish without issues, return True.

    Complexity:
    - Time: O(N^2) -> Sum of N + (N-1) + ... + 1 checks.
    - Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True






# ==========================================
# APPROACH 2: Recursive (Learning Perspective)
# ==========================================
def isSorted_Recursive(arr):
    """
    Approach 2: Recursive Check
    ---------------------------
    Visual Intuition:
    A line of dominoes. The first domino checks if it's placed correctly relative 
    to the second. If yes, it delegates the task to the second domino to check 
    the third. If any link in the chain fails, the whole check returns False.

    Steps:
    1. Base Case: If array length is 0 or 1, it's sorted -> Return True.
    2. Check First Pair: If arr[0] > arr[1], it's NOT sorted -> Return False.
    3. Recurse: Return isSorted_Recursive(arr[1:]) (Check the remaining array).
    
    Complexity:
    - Time: O(N) -> We visit each element once.
    - Space: O(N) -> Recursion stack depth.
    """
    # Helper function to handle index tracking instead of slicing (which adds overhead)
    def check(index):
        # Base Case: Reached end of array
        if index >= len(arr) - 1:
            return True
        # Check current pair
        if arr[index] > arr[index + 1]:
            return False
        # Move to next pair
        return check(index + 1)

    return check(0)

def isSorted_Recursive(arr):

    def check(index):
        #base case 
        if index>=len(arr)-1:
            True
        
        if arr[index]>arr[index+1]:
            return False
        
        check(index+1)
    
    return check(0)



# ==========================================
# APPROACH 3: Optimal (Iterative Linear Scan)
# ==========================================
def isSorted_Optimal(arr):
    """
    Approach 3: Optimal (Single Pass)
    ---------------------------------
    Visual Intuition:
    Walking up a staircase. You only need to make sure that the NEXT step is 
    higher (or same level) than the CURRENT step. If you ever have to step down 
    (arr[i] < arr[i-1]), then it's not a proper upward staircase.

    Steps:
    1. Start a loop from index 1 to N-1.
    2. Compare current element (arr[i]) with previous element (arr[i-1]).
    3. If arr[i] < arr[i-1], return False immediately.
    4. If loop completes, return True.

    Complexity:
    - Time: O(N) -> We touch each element once.
    - Space: O(1)
    """
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Sorted
    sorted_arr = [1, 2, 3, 4, 5]
    print(f"Array: {sorted_arr}")
    print(f"Brute: {isSorted_Brute(sorted_arr)}")
    print(f"Recursive: {isSorted_Recursive(sorted_arr)}")
    print(f"Optimal: {isSorted_Optimal(sorted_arr)}")
    print("-" * 30)

    # Test Case 2: Unsorted
    unsorted_arr = [1, 2, 4, 3, 5]
    print(f"Array: {unsorted_arr}")
    print(f"Optimal Result: {isSorted_Optimal(unsorted_arr)}")
    print("-" * 30)

    # Test Case 3: Duplicates (Still Sorted)
    dup_arr = [1, 1, 2, 2]
    print(f"Array: {dup_arr}")
    print(f"Optimal Result: {isSorted_Optimal(dup_arr)}")