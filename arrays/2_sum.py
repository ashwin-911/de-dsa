"""
PROBLEM: Two Sum (2Sum)
-----------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an array of integers 'arr' and an integer 'target', return indices of the 
two numbers such that they add up to 'target'.
You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

Example:
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1] (Because arr[0] + arr[1] == 9)

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Pick the first number (i). Check every other number (j) to see if they sum to target.
   - Analogy: 
     Trying every key on a keyring against every lock in the building until you 
     find the pair that works.

2. Better Approach (Hashing / Dictionary):
   - Logic: 
     We iterate through the array once. For every number 'num' we see, we calculate 
     the 'needed_value' (Target - num).
     We ask the Map: "Have I seen 'needed_value' before?"
     - If YES: We found the pair! Return current index and the index from the map.
     - If NO: Store the current 'num' and its index in the map for future checks.
   - Analogy: 
     The "Lost Partner" Board.
     Target is 10. You are number 3. You calculate you need a 7.
     You check the board. Is there a "7" posted there? 
     No? You post a note: "I am 3, looking for a partner."
     Later, number 7 walks in, sees your note, and says "Found you."

3. Optimal Approach (Two Pointers - For 'True/False' Variant):
   - Logic: 
     *Sort the array first.*
     Place one pointer at the Left (smallest) and one at the Right (largest).
     Sum them up.
     - If Sum < Target: We need a bigger number. Move Left pointer forward.
     - If Sum > Target: We need a smaller number. Move Right pointer backward.
     - If Sum == Target: Found it.
   - Note: 
     This destroys the original indices due to sorting. It is best used if we 
     only need to return the numbers themselves or return True/False.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2)
   - Space: O(1)

2. Hashing (Best for Indices):
   - Time: O(N) -> Single pass.
   - Space: O(N) -> To store the map.

3. Two Pointers (Best for Space/Existence):
   - Time: O(N log N) -> dominated by sorting.
   - Space: O(1) -> No hash map needed.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def twoSum_Brute(arr, target):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Check all pairs.
    
    Steps:
    1. Loop i from 0 to N.
    2. Loop j from i+1 to N.
    3. If arr[i] + arr[j] == target, return [i, j].
    
    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

# ==========================================
# APPROACH 2: Better/Optimal (Hashing)
# ==========================================
def twoSum_Hashing(arr, target):
    """
    Approach 2: Hashing (Recommended for Indices)
    ---------------------------------------------
    Visual Intuition:
    Reverse Lookup.
    "I have X. I need (Target-X). Is it in the history map?"

    Steps:
    1. Create empty dict 'seen'.
    2. Loop i, num in enumerate(arr).
    3. needed = target - num.
    4. If needed in seen: return [seen[needed], i].
    5. Else: seen[num] = i.
    
    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    seen = {}
    
    for i, num in enumerate(arr):
        needed = target - num
        
        # Check if the complement exists in our map
        if needed in seen:
            return [seen[needed], i]
            
        # Store current number and index
        seen[num] = i
        
    return []




# ==========================================
# APPROACH 3: Two Pointers (For Variant 2: Yes/No)
# ==========================================
def twoSum_TwoPointers(arr, target):
    """
    Approach 3: Two Pointers (Sort + Squeeze)
    -----------------------------------------
    Visual Intuition:
    The Squeezing Strategy.
    Sorted Array: [2, 3, 5, 8, 11], Target = 13
    L=2, R=11 -> Sum=13. Found!
    
    Steps:
    1. Sort the array (O(N log N)).
    2. Init left = 0, right = n-1.
    3. Loop while left < right:
       - sum = arr[left] + arr[right]
       - If sum == target: Return True
       - If sum < target: left += 1 (Need bigger sum)
       - If sum > target: right -= 1 (Need smaller sum)
    
    Complexity:
    - Time: O(N log N)
    - Space: O(1)
    """
    # Note: We sort a COPY to not mess up the original array for other tests
    sorted_arr = sorted(arr)
    
    left = 0
    right = len(sorted_arr) - 1
    
    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]
        
        if current_sum == target:
            return "YES" # Found the pair
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return "NO"

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr = [2, 6, 5, 8, 11]
    target = 14
    
    print(f"Array: {arr}, Target: {target}")
    
    # 1. Brute Force
    print(f"Brute Force Indices: {twoSum_Brute(arr, target)}")
    
    # 2. Hashing (Optimal for Indices)
    print(f"Hashing Indices:     {twoSum_Hashing(arr, target)}")
    
    # 3. Two Pointers (Optimal for Existence check)
    print(f"Two Pointers Check:  {twoSum_TwoPointers(arr, target)}")
    
    print("-" * 30)
    
    # Test Case 2: No Solution
    arr2 = [1, 2, 3]
    target2 = 10
    print(f"Array: {arr2}, Target: {target2}")
    print(f"Result: {twoSum_Hashing(arr2, target2)}")