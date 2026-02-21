"""
PROBLEM: Rearrange Array Elements by Sign
-----------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
There is an integer array 'nums' of even length consisting of an equal number of 
positive and negative integers.
You should rearrange the elements of 'nums' such that the modified array follows 
the given conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in 
   'nums' is preserved (Relative order).
3. The rearranged array begins with a positive integer.

Example:
Input: nums = [3, 1, -2, -5, 2, -4]
Output: [3, -2, 1, -5, 2, -4]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Two Separate Arrays):
   - Logic: 
     Since we need to maintain the relative order, we can simply split the 
     original array into two separate lists: one for positives and one for negatives.
     After gathering them, we interleave them back into the original array 
     (Positive at index 0, Negative at index 1, Positive at 2, etc.).
   - Analogy: 
     A gym teacher has a mixed line of boys and girls. The teacher separates them 
     into two distinct lines. Then, to pair them up, the teacher pulls one from 
     the boys' line, then one from the girls' line, repeatedly.

2. Optimal Approach (Single Pass with Two Pointers):
   - Logic: 
     We already know exactly where the numbers need to go:
     - Positives ALWAYS go to even indices (0, 2, 4, 6...).
     - Negatives ALWAYS go to odd indices (1, 3, 5, 7...).
     
     Instead of storing them in separate arrays first, we can create a result 
     array of the same size. We use two pointers (`pos_idx` starting at 0, 
     `neg_idx` starting at 1). As we traverse the original array, we drop the 
     numbers directly into their designated slots and increment that specific 
     pointer by 2.
   - Analogy: 
     A Traffic Director at a parking lot. Red cars (Negatives) must park in odd 
     spots. Blue cars (Positives) must park in even spots. As a car drives up, 
     the director points them directly to the next available spot of their color.

Note on Space Complexity: 
An O(1) space solution that operates in O(N) time while maintaining relative order 
does not exist. Therefore, the O(N) space approach is the standard optimal solution.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N) + O(N) = O(2N) -> Two passes (one to split, one to merge).
   - Space: O(N) -> For the two separate positive and negative lists.

2. Optimal Approach:
   - Time: O(N) -> Single pass.
   - Space: O(N) -> For the result array.
"""

# ==========================================
# APPROACH 1: Brute Force (Two Arrays)
# ==========================================
def rearrangeArray_Brute(nums):
    """
    Approach 1: Brute Force (Separation and Merging)
    ------------------------------------------------
    Visual Intuition:
    Splitting the deck of cards into red and black piles, then perfectly shuffles 
    them back together one by one.

    Steps:
    1. Create two lists: `pos` and `neg`.
    2. Iterate through `nums` and append to `pos` if > 0, else to `neg`.
    3. Loop i from 0 to N/2.
    4. Overwrite `nums[2*i] = pos[i]`.
    5. Overwrite `nums[2*i + 1] = neg[i]`.
    6. Return `nums`.

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    n = len(nums)
    pos = []
    neg = []
    
    # Step 1 & 2: Segregate
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
            
    # Step 3, 4 & 5: Interleave
    for i in range(len(pos)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
        
    return num



# ==========================================
# APPROACH 2: Optimal (Single Pass)
# ==========================================
def rearrangeArray_Optimal(nums):
    """
    Approach 2: Optimal (Direct Placement)
    --------------------------------------
    Visual Intuition:
    The "Direct Deposit" method. We know exactly where the next positive or negative 
    number belongs, so we skip the intermediate holding arrays and place them 
    straight into the final result.

    Steps:
    1. Create an `ans` array of size N filled with 0s.
    2. Initialize `pos_idx = 0` and `neg_idx = 1`.
    3. Iterate through `nums`:
       - If num > 0: Place at `ans[pos_idx]`, increment `pos_idx` by 2.
       - If num < 0: Place at `ans[neg_idx]`, increment `neg_idx` by 2.
    4. Return `ans`.

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    n = len(nums)
    ans = [0] * n
    
    pos_idx = 0
    neg_idx = 1
    
    for num in nums:
        if num > 0:
            ans[pos_idx] = num
            pos_idx += 2
        else:
            ans[neg_idx] = num
            neg_idx += 2
            
    return ans



        
# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    arr1 = [3, 1, -2, -5, 2, -4]
    print(f"Original Array: {arr1}")
    
    # Passing a copy so Brute Force doesn't mutate the array before Optimal runs
    print(f"Brute Force:    {rearrangeArray_Brute(arr1.copy())}")
    print(f"Optimal:        {rearrangeArray_Optimal(arr1)}")
    
    print("-" * 30)
    
    # Test Case 2: All positives clustered at start
    arr2 = [1, 2, 3, -1, -2, -3]
    print(f"Original Array: {arr2}")
    print(f"Optimal:        {rearrangeArray_Optimal(arr2)}")