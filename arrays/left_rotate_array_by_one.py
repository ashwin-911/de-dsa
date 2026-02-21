-"""
PROBLEM: Left Rotate an Array by One Place
------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an array of N integers, rotate the array to the left by one position.
The first element moves to the end, and everyone else shifts one step left.

Example:
Input: [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Using Slicing / New Array):
   - Logic: Python's slicing makes this trivial. We can take the sub-array from 
     index 1 to the end, and concatenate the sub-array containing just index 0 
     at the very back.
   - Analogy: Taking a photo of the queue excluding the first person, and 
     Photoshopping the first person at the end. You create a new image.

2. Optimal Approach (In-Place Shifting):
   - Logic: We want to do this without creating a new array (O(1) space).
     1. Store the first element (arr[0]) in a temporary pocket.
     2. Shift every other element one step to the left (arr[i] = arr[i+1]).
     3. Place the element from the pocket into the last empty spot.
   - Analogy: A line of people. The first person steps out of line. 
     Everyone else takes one step forward. The first person walks to the 
     back and joins the end of the line.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N) -> Copying elements to new list.
   - Space: O(N) -> Creating a new list of size N.

2. Optimal Approach:
   - Time: O(N) -> We iterate through the array once to shift.
   - Space: O(1) -> We modify the array in-place using only one temp variable.
"""

# ==========================================
# APPROACH 1: Brute Force (Slicing / New List)
# ==========================================
def leftRotate_Brute(arr):
    """
    Approach 1: Brute Force (Slicing)
    ---------------------------------
    Visual Intuition:
    Cut the head off the snake and tape it to the tail. 
    However, this creates a 'new snake' (new memory allocation).

    Steps:
    1. Create a new list containing arr[1] to arr[N-1].
    2. Append arr[0] to this new list.
    3. Return the new list.

    Complexity:
    - Time: O(N)
    - Space: O(N) (New array created)
    """
    n = len(arr)
    if n <= 1:
        return arr
        
    # In Python, slicing creates copies
    # new_arr = arr[1:] + arr[:1]
    # But to be explicit without slicing shortcuts:
    new_arr = []
    for i in range(1, n):
        new_arr.append(arr[i])
    new_arr.append(arr[0])
    
    return new_arr



# ==========================================
# APPROACH 2: Optimal (In-Place Shift)
# ==========================================
def leftRotate_Optimal(arr):
    """
    Approach 2: Optimal (In-Place Shift)
    ------------------------------------
    Visual Intuition:
    The "Temp Pocket" Strategy. 
    Imagine a row of chairs. 
    1. Person in Chair 0 stands up and moves aside (temp = arr[0]).
    2. Person in Chair 1 moves to Chair 0.
    3. Person in Chair 2 moves to Chair 1.
    ...
    4. Person in Chair N-1 moves to Chair N-2.
    5. The empty Chair N-1 is filled by the person who stood aside (temp).

    Steps:
    1. Save arr[0] in a variable 'temp'.
    2. Loop from i = 1 to N-1:
       - Set arr[i-1] = arr[i] (Pull value from right to left).
    3. Set arr[n-1] = temp.

    Complexity:
    - Time: O(N)
    - Space: O(1) (Modified in-place)
    """
    n = len(arr)
    if n <= 1:
        return arr
        
    # Step 1: Store the first element
    temp = arr[0]
    
    # Step 2: Shift elements to the left
    # We iterate from 1 to n-1
    for i in range(1, n):
        arr[i-1] = arr[i]
        
    # Step 3: Put the first element at the back
    arr[n-1] = temp
    
    return arr




# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr1 = [1, 2, 3, 4, 5]
    print(f"Original Array: {arr1}")
    
    # Brute Force (Returns new array)
    result_brute = leftRotate_Brute(arr1)
    print(f"Brute Force Result: {result_brute}")
    
    # Test Case 2: Optimal (Modifies in-place)
    # Re-using arr1 logic, but let's use a fresh array
    arr2 = [10, 20, 30, 40]
    print(f"\nOriginal Array 2: {arr2}")
    
    leftRotate_Optimal(arr2)
    print(f"Optimal Result (In-Place): {arr2}")
    
    # Edge Case: Single Element
    arr3 = [99]
    leftRotate_Optimal(arr3)
    print(f"\nEdge Case [99]: {arr3}")