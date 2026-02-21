"""
PROBLEM: Remove Duplicates from Sorted Array
--------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an integer array sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements 
should be kept the same.
Return the number of unique elements (k). The first k elements of the array should 
hold the unique values.

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Using a Set):
   - Logic: A Set data structure automatically filters out duplicates. 
     We can insert all elements into a Set, and then put them back into the 
     array from the beginning.
   - Analogy: Dump all the dirty laundry (array) into a magical washing machine (Set)
     that destroys duplicates. Then take the clean clothes out and fold them 
     back into the drawer (array) one by one.

2. Optimal Approach (Two Pointers):
   - Logic: Since the array is SORTED, duplicates are always grouped together.
     We use two pointers:
     - Pointer 'i': Keeps track of the last unique element we successfully placed.
     - Pointer 'j': Scouts ahead to find a NEW unique number.
     
     Whenever 'j' finds a number different from 'i', we move 'i' forward and 
     copy that new number there.
   - Analogy: Imagine 'i' is a builder constructing a wall of unique bricks. 
     'j' is a supplier. 'j' keeps running through the pile of bricks. 
     If 'j' finds a brick that looks exactly like the one 'i' just laid, he skips it.
     If 'j' finds a NEW type of brick, he hands it to 'i', who places it 
     right next to the previous one.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N log N) or O(N) -> Depends on Set implementation (insertions). 
     Plus O(N) to copy back.
   - Space: O(N) -> To store the Set.

2. Optimal Approach:
   - Time: O(N) -> Single pass with pointer 'j'.
   - Space: O(1) -> No extra data structures used.
"""

# ==========================================
# APPROACH 1: Brute Force (Using Set)
# ==========================================
def removeDuplicates_Brute(arr):
    """
    Approach 1: Brute Force (HashSet)
    ---------------------------------
    Visual Intuition:
    We need a temporary container that refuses to hold duplicates. A Set is perfect.
    We just pour everything into the Set, and then pour the Set back into the array.

    Steps:
    1. Create a Set and add all elements from arr to it.
    2. Sort the set (sets are unordered, but we need sorted result).
    3. Iterate through the set and overwrite arr[0], arr[1], etc.
    4. Return the size of the set.

    Complexity:
    - Time: O(N) to insert + O(N log N) to sort the unique elements (if set ruins order).
    - Space: O(N) for the Set.
    """
    if not arr:
        return 0
        
    # Use a set to store unique elements
    unique_set = set(arr)
    
    # Sort them to maintain the required order
    # (Note: In Python, just casting set to list doesn't guarantee sort)
    unique_list = sorted(list(unique_set))
    
    # Place them back into the original array
    for i in range(len(unique_list)):
        arr[i] = unique_list[i]
        
    return len(unique_list)







# ==========================================
# APPROACH 2: Optimal (Two Pointers)
# ==========================================
def removeDuplicates_Optimal(arr):
    """
    Approach 2: Optimal (Two Pointers)
    ----------------------------------
    Visual Intuition:
    'i' is the "Keeper". It stands on the last valid unique number.
    'j' is the "Seeker". It runs ahead looking for something different.
    
    arr = [1, 1, 1, 2, 2, 3]
           ^     ^
           i     j
    
    - j sees 1 (same as i): Ignore.
    - j moves to 2 (different!): 
      1. Move i forward (make space).
      2. Copy 2 into i's new spot.
    
    Result: The front of the array becomes [1, 2, 3, ...].

    Steps:
    1. Initialize i = 0.
    2. Loop j from 1 to N-1.
    3. If arr[j] != arr[i]:
       - Increment i.
       - arr[i] = arr[j].
    4. Return i + 1 (because index is 0-based, count is index+1).

    Complexity:
    - Time: O(N) -> We traverse the array once.
    - Space: O(1) -> In-place modification.
    """
    if not arr:
        return 0
        
    i = 0 # The Keeper
    
    for j in range(1, len(arr)):
        # If Seeker finds a new unique element
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
            
    # Length of unique part is index + 1
    return i + 1







# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 1, 2, 2, 2, 3, 3]
    print(f"Original Array: {arr1}")
    
    # Note: We pass a copy for Brute because it modifies in-place
    k_brute = removeDuplicates_Brute(arr1.copy())
    print(f"Brute Force Result (Count): {k_brute}")
    
    # Test Case 2 (Optimal)
    arr2 = [1, 1, 2, 2, 2, 3, 3]
    k_optimal = removeDuplicates_Optimal(arr2)
    print(f"Optimal Result (Count): {k_optimal}")
    print(f"Modified Array (First {k_optimal} elements): {arr2[:k_optimal]}")
    
    print("-" * 30)
    
    # Test Case 3: All duplicates
    arr3 = [10, 10, 10]
    k3 = removeDuplicates_Optimal(arr3)
    print(f"All Duplicates Array: [10, 10, 10]")
    print(f"Unique Count: {k3}")
    print(f"Modified Array: {arr3[:k3]}")