"""
PROBLEM: Left Rotate an Array by D Places
-----------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given an array of N integers and an integer D, rotate the array to the left by D positions.
Note: If D is greater than N, you should effectively rotate by (D % N).

Example:
Input: arr = [1, 2, 3, 4, 5, 6, 7], D = 3
Output: [4, 5, 6, 7, 1, 2, 3]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Using Temp Array):
   - Logic: If we want to move the first D elements to the back, we can just:
     1. Copy the first D elements into a temporary list.
     2. Shift the remaining (N-D) elements to the front of the original array.
     3. Copy the temporary list back into the end of the original array.
   - Analogy: "Cutting the Deck" in a card game. You take the top stack of cards (D),
     hold it in your hand (temp), and place it at the bottom of the deck.

2. Optimal Approach (Reversal Algorithm):
   - Logic: A clever mathematical trick involving reversals.
     To rotate Left by D:
     1. Reverse the first D elements (0 to D-1).
     2. Reverse the remaining elements (D to N-1).
     3. Reverse the WHOLE array (0 to N-1).
   - Visual:
     Arr: [1, 2, 3, 4, 5], D=2
     Rev(0,1) -> [2, 1, 3, 4, 5]
     Rev(2,4) -> [2, 1, 5, 4, 3]
     Rev(All) -> [3, 4, 5, 1, 2] -> ROTATED!

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N) -> We touch every element (copy D, shift N-D, paste D).
   - Space: O(D) -> We need a temporary array to store D elements.

2. Optimal Approach:
   - Time: O(2N) -> We reverse parts of the array (approximates to 2 passes).
   - Space: O(1) -> Done entirely in-place.
"""

# ==========================================
# APPROACH 1: Brute Force (Temp Array)
# ==========================================
def leftRotate_Brute(arr, d):
    """
    Approach 1: Brute Force (Temp Storage)
    --------------------------------------
    Visual Intuition:
    The "Cut and Paste" method.
    We physically cut the first chunk (size D) and paste it at the end.

    Steps:
    1. Normalize D: d = d % n.
    2. Store arr[0...d-1] in 'temp'.
    3. Shift arr[d...n-1] to the left (to index 0).
    4. Copy 'temp' into arr[n-d...n-1].

    Complexity:
    - Time: O(d) + O(n-d) + O(d) = O(N)
    - Space: O(D) (for temp array)
    """
    n = len(arr)
    d = d % n  # Handle cases where D > N
    if d == 0: return arr

    # Step 1: Store first d elements
    temp = arr[:d]

    # Step 2: Shift the rest of the array to the left
    # We move element at index 'i' to 'i-d'
    for i in range(d, n):
        arr[i - d] = arr[i]

    # Step 3: Put back the temp elements
    for i in range(d):
        arr[n - d + i] = temp[i]

    return arr



# ==========================================
# APPROACH 2: Optimal (Reversal Algorithm)
# ==========================================
def leftRotate_Optimal(arr, d):
    """
    Approach 2: Optimal (Reversal Algorithm)
    ----------------------------------------
    Visual Intuition:
    The "Flip, Flip, Flip" Trick.
    Imagine a shirt turned inside out. If you flip the left sleeve, then the right 
    sleeve, and then the whole shirt, it magically aligns correctly (this is an 
    abstract analogy, but the math holds!).

    Steps:
    1. Normalize D: d = d % n.
    2. Reverse the first part: arr[0] to arr[d-1].
    3. Reverse the second part: arr[d] to arr[n-1].
    4. Reverse the whole array: arr[0] to arr[n-1].

    Complexity:
    - Time: O(2N) -> Reversing takes linear time.
    - Space: O(1) -> No extra arrays used.
    """
    n = len(arr)
    d = d % n
    if d == 0: return arr

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse first D elements
    reverse(0, d - 1)

    # Step 2: Reverse remaining N-D elements
    reverse(d, n - 1)

    # Step 3: Reverse the whole array
    reverse(0, n - 1)
    
    return arr





# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    d1 = 3
    print(f"Original Array: {arr1}, D = {d1}")
    
    # Brute Force (Modifies in place, so passing copy)
    res_brute = leftRotate_Brute(arr1.copy(), d1)
    print(f"Brute Result: {res_brute}")

    # Test Case 2: Optimal
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    d2 = 3
    leftRotate_Optimal(arr2, d2)
    print(f"Optimal Result: {arr2}")

    # Test Case 3: D > N (Modulo Check)
    arr3 = [1, 2, 3]
    d3 = 4  # Effectively rotates by 1
    leftRotate_Optimal(arr3, d3)
    print(f"\nEdge Case (D=4, N=3): {arr3}")