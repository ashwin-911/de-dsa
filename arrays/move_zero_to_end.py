"""
PROBLEM: Move Zeros to End
--------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.
Note: You must do this in-place without making a copy of the array.

Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Using Temp Array):
   - Logic: 
     1. Create a temporary list. 
     2. Scan the original array and copy ONLY the non-zero numbers into the temp list.
     3. Fill the rest of the temp list with zeros until it matches the original size.
     4. Copy the temp list back to the original array.
   - Analogy: Taking all the "good apples" (non-zeros) out of a basket and putting 
     them into a new box. Then filling the empty space in the new box with "packing 
     peanuts" (zeros). Finally, dumping the new box back into the basket.

2. Optimal Approach (Two Pointers / Partitioning):
   - Logic: 
     We partition the array into "Non-Zero" and "Zero" regions.
     - Pointer 'i': Always points to the first ZERO found so far (the placeholder 
       waiting to be filled).
     - Pointer 'j': Scans ahead to find a NON-ZERO number.
     
     Whenever 'j' finds a non-zero, we SWAP it with the zero at 'i'. 
     Then 'i' moves forward to the next zero.
   - Visual:
     [1, 0, 2, 0, 3]
         ^  ^
         i  j
     
     'j' sees 2 (non-zero). SWAP with 'i'.
     [1, 2, 0, 0, 3]
            ^     ^
            i     j (moves)

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N) -> Single pass to filter, single pass to fill.
   - Space: O(N) -> Temporary array used.

2. Optimal Approach:
   - Time: O(N) -> Single pass traversal.
   - Space: O(1) -> In-place operations.
"""

# ==========================================
# APPROACH 1: Brute Force (Temp Array)
# ==========================================
def moveZeros_Brute(arr):
    """
    Approach 1: Brute Force (Temp Array)
    ------------------------------------
    Visual Intuition:
    Filter out the zeros, then pad the end.

    Steps:
    1. Create 'temp' list.
    2. Iterate arr: if x != 0, append to temp.
    3. Calculate remaining zeros needed: N - len(temp).
    4. Extend temp with that many zeros.
    5. Copy temp back to arr.

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    n = len(arr)
    temp = []
    
    # Step 1: Collect non-zeros
    for num in arr:
        if num != 0:
            temp.append(num)
            
    # Step 2: Fill the rest with zeros
    while len(temp) < n:
        temp.append(0)
        
    # Step 3: Copy back to original
    for i in range(n):
        arr[i] = temp[i]
        
    return arr



# ==========================================
# APPROACH 2: Optimal (Two Pointers)
# ==========================================
def moveZeros_Optimal(arr):
    """
    Approach 2: Optimal (Two Pointers)
    ----------------------------------
    Visual Intuition:
    The "Snowplow" Method.
    Pointer 'j' acts like a plow pushing through the array. 
    Pointer 'i' waits at the first 'hole' (zero). 
    When 'j' finds a solid rock (non-zero), it throws it into the hole at 'i', 
    and the hole effectively moves to where the rock was.

    Steps:
    1. Find the first zero: Iterate to find index 'j' where arr[j] == 0. 
       Set 'i' = j. (If no zero found, return).
    2. Start loop 'j' from i+1 to N-1.
    3. If arr[j] != 0:
       - Swap arr[i] and arr[j].
       - Increment i (move to next zero).

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    n = len(arr)
    
    # Step 1: Find the first zero
    i = -1
    for k in range(n):
        if arr[k] == 0:
            i = k
            break
            
    # If no zero is found, array is already done
    if i == -1:
        return arr
        
    # Step 2: Move pointers
    # i points to the zero, j points to the current element check
    for j in range(i + 1, n):
        if arr[j] != 0:
            # Swap the non-zero (j) with the zero (i)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    return arr


# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr1 = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(f"Original Array: {arr1}")
    
    # Brute Force (Passing copy)
    res_brute = moveZeros_Brute(arr1.copy())
    print(f"Brute Result: {res_brute}")
    
    # Optimal
    moveZeros_Optimal(arr1)
    print(f"Optimal Result: {arr1}")
    
    # Test Case 2: No Zeros
    arr2 = [1, 2, 3, 4]
    moveZeros_Optimal(arr2)
    print(f"\nNo Zeros Case: {arr2}")
    
    # Test Case 3: All Zeros
    arr3 = [0, 0, 0]
    moveZeros_Optimal(arr3)
    print(f"All Zeros Case: {arr3}")