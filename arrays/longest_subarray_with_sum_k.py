"""
PROBLEM: Longest Subarray with Sum K (Positives)
------------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given an array containing N **positive** integers and an integer K, 
find the length of the longest subarray with a sum equal to K.

Example:
Input: arr = [1, 2, 3, 1, 1, 1, 1], K = 3
Output: 3 
(Subarrays with sum 3: [1,2], [3], [1,1,1]. Longest is [1,1,1] with length 3)

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Generate all possible subarrays. Calculate the sum of each. 
     If sum == K, compare its length with the max length found so far.
   - Analogy: 
     Cutting every possible slice of a cake to see which one weighs exactly K grams, 
     then keeping the longest valid slice.

2. Better Approach (Hashing / Prefix Sum):
   - Logic: 
     Math property: SubarraySum(i, j) = PrefixSum(j) - PrefixSum(i).
     If we are at index 'j' with current sum 'S', we look for a previous prefix 
     sum of 'S - K'. If that existed at index 'i', then the subarray from i+1 to j 
     must be K.
     We store {PrefixSum: Index} in a Hash Map.
   - Note: 
     This approach works for Negatives too! But requires O(N) space.
   - Analogy: 
     Keeping a running log of total distance traveled. If you are at mile 50, 
     and you want to know if you traveled exactly 10 miles recently, you check 
     your log to see if you were ever at mile 40.

3. Optimal Approach (Two Pointers / Sliding Window):
   - Logic: 
     Since numbers are POSITIVE, the sum only grows if we add numbers and 
     shrinks if we remove them.
     - Pointer 'right': Expands the window (adds element).
     - Pointer 'left': Shrinks the window (removes element) if sum > K.
     If sum == K, we record the length.
   - Analogy: 
     The "Caterpillar". The head (right) eats leaves to grow. If it gets too fat 
     (sum > K), the tail (left) moves forward to shrink.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^3) or O(N^2) depending on implementation.
   - Space: O(1)

2. Better Approach (Hashing):
   - Time: O(N) -> Single pass.
   - Space: O(N) -> Hash Map storage.

3. Optimal Approach (Two Pointers):
   - Time: O(2N) -> Each element is visited at most twice (once by right, once by left).
   - Space: O(1) -> No extra data structures.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def longestSubarray_Brute(arr, k):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Try every start and end point.

    Steps:
    1. Loop i from 0 to N.
    2. Loop j from i to N.
    3. Calculate sum of arr[i...j].
    4. If sum == k, update max_len.
    
    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    n = len(arr)
    max_len = 0
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            
            if current_sum == k:
                max_len = max(max_len, j - i + 1)
            
            # Optimization: If sum exceeds k, no point looking further (since positives only)
            if current_sum > k:
                break
                
    return max_len




            


# ==========================================
# APPROACH 2: Better (Hashing / Prefix Sum)
# ==========================================
def longestSubarray_Better(arr, k):
    """
    Approach 2: Hashing (Prefix Sum)
    --------------------------------
    Visual Intuition:
    Reverse Engineering using a history log.
    Current Sum = 15, Target = 5. 
    Did I ever see a Sum of 10 before? Yes, at index 2.
    So the path from index 3 to now is 5.

    Steps:
    1. Init preSumMap = {0: -1} (Base case: Sum 0 at index -1).
    2. Loop through arr, calculating cumulative sum.
    3. Check if (sum - k) exists in map.
       - Yes: len = current_index - map[sum-k]. Update max_len.
    4. If sum is NOT in map, add it. 
       (Important: If sum exists, DON'T update it, we want the *earliest* index for *longest* subarray).

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    preSumMap = {}
    current_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # Case 1: The prefix sum itself is K
        if current_sum == k:
            max_len = max(max_len, i + 1)
            
        # Case 2: The prefix sum - k exists in history
        rem = current_sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            max_len = max(max_len, length)
            
        # Case 3: Add to map if not present
        if current_sum not in preSumMap:
            preSumMap[current_sum] = i
            
    return max_len






# ==========================================
# APPROACH 3: Optimal (Two Pointers)
# ==========================================
def longestSubarray_Optimal(arr, k):
    """
    Approach 3: Optimal (Sliding Window)
    ------------------------------------
    Visual Intuition:
    The Greedy Caterpillar.
    - Right pointer moves to EAT (add sum).
    - If sum > k, Left pointer moves to DIGEST/SHRINK (subtract sum).
    - If sum == k, measure the size.

    Steps:
    1. Init left = 0, right = 0, sum = arr[0], max_len = 0.
    2. Loop while right < N:
       - While sum > k and left <= right: Subtract arr[left], increment left.
       - If sum == k: Update max_len.
       - Increment right.
       - If right < N: Add arr[right] to sum.

    Complexity:
    - Time: O(2N) (Each element added once, removed once).
    - Space: O(1).
    """
    n = len(arr)
    left = 0
    right = 0
    current_sum = arr[0]
    max_len = 0
    
    while right < n:
        # Shrink from left if sum is too high
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
            
        # Check if we hit the target
        if current_sum == k:
            max_len = max(max_len, right - left + 1)
            
        # Move right forward
        right += 1
        if right < n:
            current_sum += arr[right]
            
    return max_len



        
    

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr1 = [1, 2, 3, 1, 1, 1, 1]
    k1 = 3
    print(f"Array: {arr1}, K: {k1}")
    print(f"Brute:   {longestSubarray_Brute(arr1, k1)}")
    print(f"Better:  {longestSubarray_Better(arr1, k1)}")
    print(f"Optimal: {longestSubarray_Optimal(arr1, k1)}")
    
    print("-" * 30)
    
    # Test Case 2: No subarray found
    arr2 = [1, 2, 3]
    k2 = 10
    print(f"Array: {arr2}, K: {k2}")
    print(f"Optimal: {longestSubarray_Optimal(arr2, k2)}")
    
    # Test Case 3: Single element match
    arr3 = [2, 3, 5]
    k3 = 5
    print(f"Array: {arr3}, K: {k3}")
    print(f"Optimal: {longestSubarray_Optimal(arr3, k3)}")