"""
PROBLEM: Second Largest Element in an Array (without sorting)
-------------------------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy/Medium

Problem Statement:
Given an array of size N, find the second largest distinct element from an array.
If the second largest element doesn't exist (e.g., all elements are same), return -1.

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Sorting):
   - Logic: Sort the array in ascending order. The largest is at index n-1.
     The second largest is the first element from the back (n-2, n-3...) 
     that is NOT equal to the largest.
   - Analogy: Line everyone up by height. Pick the tallest. Then walk down 
     the line until you find someone shorter.

2. Better Approach (Two Pass Scan):
   - Logic: 
     Pass 1: Find the 'Champion' (Largest element).
     Pass 2: Find the 'Runner-up' (Largest element that is != Champion).
   - Analogy: First look through the crowd to find the King. Then look 
     through the crowd again to find the Prince (best of the rest).

3. Optimal Approach (Single Pass / "King and Prince"):
   - Logic: We can find both in a single walk. Keep two variables: 
     'largest' and 'second'.
   - As we walk:
     Case A: If current > largest -> Old King becomes Prince, Current becomes King.
     Case B: If current > second (but < largest) -> Current becomes Prince.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N log N) -> Sorting takes the most time.
   - Space: O(1) -> If we ignore space taken by sorting algo.

2. Better Approach:
   - Time: O(2N) -> We traverse the array twice.
   - Space: O(1) -> No extra data structures.

3. Optimal Approach:
   - Time: O(N) -> Single pass traversal.
   - Space: O(1) -> Only two variables used.
"""

# ==========================================
# APPROACH 1: Brute Force (Sorting)
# ==========================================
def getSecondLargest_Brute(arr):
    n = len(arr)
    if n < 2:
        return -1
        
    # Sort the array -> O(N log N)
    arr.sort()
    
    largest = arr[n - 1]
    
    # Traverse from second last element backwards to find distinct
    for i in range(n - 2, -1, -1):
        if arr[i] != largest:
            return arr[i]
            
    return -1






# ==========================================
# APPROACH 2: Better (Two Passes)
# ==========================================
def getSecondLargest_Better(arr):
    n = len(arr)
    if n < 2:
        return -1
        
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Pass 1: Find Largest
    for num in arr:
        if num > largest:
            largest = num
            
    # Pass 2: Find Second Largest (strictly smaller than largest)
    for num in arr:
        if num > second_largest and num != largest:
            second_largest = num
            
    if second_largest == float('-inf'):
        return -1
        
    return second_largest





# ==========================================
# APPROACH 3: Optimal (Single Pass)
# ==========================================
def getSecondLargest_Optimal(arr):
    n = len(arr)
    if n < 2:
        return -1
        
    largest = float('-inf')
    second = float('-inf')
    
    for num in arr:
        # Case 1: New Largest found
        if num > largest:
            second = largest  # Old largest becomes second
            largest = num     # Update largest
            
        # Case 2: Element is smaller than largest, but bigger than second
        elif num > second and num != largest:
            second = num
            
    if second == float('-inf'):
        return -1
        
    return second






# ==========================================
# DRIVER CODE (Test your logic here)
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    test_arr = [1, 2, 4, 7, 7, 5]
    print(f"Original Array: {test_arr}")
    
    # Pass a copy to Brute because it sorts (modifies) the array
    print(f"Brute Force: {getSecondLargest_Brute(test_arr.copy())}")
    print(f"Better (2 Pass): {getSecondLargest_Better(test_arr)}")
    print(f"Optimal (1 Pass): {getSecondLargest_Optimal(test_arr)}")
    
    print("-" * 30)
    
    # Test Case 2: All duplicates
    same_arr = [10, 10, 10]
    print(f"Duplicates Array: {same_arr}")
    print(f"Optimal Result: {getSecondLargest_Optimal(same_arr)}") 
    # Expected: -1