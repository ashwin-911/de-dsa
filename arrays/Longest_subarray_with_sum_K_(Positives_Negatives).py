"""
PROBLEM: Longest Subarray with Sum K (Positives + Negatives)
------------------------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given an array containing N integers (both positive and negative) and an integer K, 
find the length of the longest subarray with a sum equal to K.

Example:
Input: arr = [1, -1, 5, -2, 3], K = 3
Output: 4 
(Subarray [1, -1, 5, -2] sums to 3 and has length 4)

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Why Sliding Window Fails:
   - In the positives-only version, if Sum > K, we knew for sure we had to shrink 
     from the left to reduce the sum.
   - With negatives, shrinking from the left might actually INCREASE the sum 
     (removing a -5 increases sum by 5). We lose the ability to make greedy decisions.

2. Optimal Approach (Hashing / Prefix Sum):
   - Logic: 
     We use the formula: SubarraySum = CurrentPrefixSum - PreviousPrefixSum.
     We want SubarraySum to be K.
     So: K = CurrentPrefixSum - PreviousPrefixSum
     Rearranging: PreviousPrefixSum = CurrentPrefixSum - K.
     
     As we iterate, we calculate the 'CurrentPrefixSum'. We then ask the Hash Map:
     "Have I seen a sum of (CurrentPrefixSum - K) before?"
     - If YES: It means the subarray strictly between that previous index and 
       now has the sum K. We calculate the distance.
     - If NO: We store the current sum and its index in the map.

   - Key Detail: 
     If the same sum occurs multiple times, DO NOT update the index in the map. 
     We want the *first* occurrence (leftmost) to ensure the subarray is the *longest*.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2) -> Check all subarrays.
   - Space: O(1)

2. Optimal Approach (Hashing):
   - Time: O(N) -> Single pass traversal.
   - Space: O(N) -> To store the Prefix Sum Map.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def longestSubarray_Brute(arr, k):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Generate every possible slice of the array and weigh it.

    Steps:
    1. Loop i from 0 to N.
    2. Loop j from i to N.
    3. Calculate sum of slice arr[i...j].
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
                
    return max_len

# ==========================================
# APPROACH 2: Optimal (Hashing)
# ==========================================
def longestSubarray_Optimal(arr, k):
    """
    Approach 2: Optimal (Prefix Sum Map)
    ------------------------------------
    Visual Intuition:
    The "Reverse Lookup".
    Imagine walking up a mountain (sum increases/decreases). You are currently at 
    Height 10. You want to know if you made a climb of exactly 3 meters recently.
    You check your logbook: "Did I ever stand at Height 7 (10-3)?"
    If yes, at time T=2, and now is T=10, then the climb lasted 8 minutes.

    Steps:
    1. Initialize map: preSumMap = {}.
    2. Loop i through array.
    3. Add arr[i] to current_sum.
    4. Check 1: If current_sum == k, max_len = i + 1.
    5. Check 2: If (current_sum - k) in map:
       - length = i - preSumMap[current_sum - k]
       - max_len = max(max_len, length)
    6. Check 3: If current_sum NOT in map:
       - preSumMap[current_sum] = i
       (Crucial: Only add if not present, to keep the earliest index).

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    n = len(arr)
    preSumMap = {}
    current_sum = 0
    max_len = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        # Case 1: The prefix sum from index 0 is exactly K
        if current_sum == k:
            max_len = max(max_len, i + 1)
            
        # Case 2: We found a subarray somewhere in the middle
        rem = current_sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            max_len = max(max_len, length)
            
        # Case 3: Store the sum only if we haven't seen it before
        # This ensures we keep the leftmost index for maximum length
        if current_sum not in preSumMap:
            preSumMap[current_sum] = i
            
    return max_len

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Negatives involved
    arr1 = [1, -1, 5, -2, 3]
    k1 = 3
    print(f"Array: {arr1}, K: {k1}")
    print(f"Brute Force: {longestSubarray_Brute(arr1, k1)}")
    print(f"Optimal:     {longestSubarray_Optimal(arr1, k1)}")
    
    print("-" * 30)
    
    # Test Case 2: Subarray with zeros (Zeros don't change sum but increase length)
    arr2 = [1, 2, 3, 0, 0, 0]
    k2 = 6
    # [1,2,3] sums to 6 (len 3). [1,2,3,0,0,0] also sums to 6 (len 6).
    # Code should return 6.
    print(f"Array: {arr2}, K: {k2}")
    print(f"Optimal:     {longestSubarray_Optimal(arr2, k2)}")
    
    # Test Case 3: Negative K
    arr3 = [-2, -1, 2, 1]
    k3 = -3
    # Subarray [-2, -1] sums to -3
    print(f"Array: {arr3}, K: {k3}")
    print(f"Optimal:     {longestSubarray_Optimal(arr3, k3)}")