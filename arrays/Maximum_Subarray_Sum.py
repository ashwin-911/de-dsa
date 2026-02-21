"""
PROBLEM: Kadane's Algorithm (Maximum Subarray Sum)
--------------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Calculate the sum of every possible subarray.
     Start at i=0, end at j=0..N.
     Start at i=1, end at j=1..N.
     Keep track of the maximum sum found.
   - Analogy: 
     Trying every single item on the menu and every combination of items 
     to see which meal is the heaviest.

2. Optimal Approach (Kadane's Algorithm):
   - Logic: 
     The "Discard the Baggage" Strategy.
     We iterate through the array, adding numbers to a `current_sum`.
     
     The Core Rule:
     **"If my current sum becomes negative, I am better off starting fresh."**
     
     Why? Because a negative sum is "baggage". If I carry a sum of -5 into the 
     next number (say, 10), the total becomes 5. 
     If I had just started fresh at 10, the total would be 10. 
     10 > 5. So, carrying negative debt never helps maximize future sums.

     Algorithm:
     1. Add number to `current_sum`.
     2. Update `max_sum` if `current_sum` is higher.
     3. If `current_sum` < 0, reset `current_sum` to 0.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2)
   - Space: O(1)

2. Optimal Approach (Kadane's):
   - Time: O(N) -> Single pass.
   - Space: O(1) -> Only 2 variables.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def maxSubArray_Brute(nums):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Generate all subarrays, sum them up.

    Steps:
    1. Init max_sum = -infinity.
    2. Loop i from 0 to N.
    3. Loop j from i to N.
    4. Calculate sum(nums[i:j+1]).
    5. Update max_sum.

    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
            
    return max_sum







# ==========================================
# APPROACH 2: Optimal (Kadane's Algorithm)
# ==========================================
def maxSubArray_Kadane(nums):
    """
    Approach 2: Kadane's Algorithm
    ------------------------------
    Visual Intuition:
    The "Bank Account" Analogy.
    - You walk down the street picking up money (positive nums) or paying fines (negative nums).
    - You keep a running balance (`current_sum`).
    - You record your highest ever balance (`max_sum`).
    - If your balance drops below $0 (bankruptcy), you declare bankruptcy, 
      throw away the debt, and reset your balance to $0 to start fresh.

    Steps:
    1. Init max_sum = -infinity (to handle all negative arrays).
    2. Init current_sum = 0.
    3. Iterate through nums:
       - current_sum += num
       - max_sum = max(max_sum, current_sum)
       - if current_sum < 0: current_sum = 0
    
    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        # Capture the max BEFORE resetting (crucial for all-negative arrays)
        if current_sum > max_sum:
            max_sum = current_sum
            
        # If we drop below zero, reset (carry no debt)
        if current_sum < 0:
            current_sum = 0
            
    return max_sum


def maxSubArray_Kadane(nums):

    max_sum=float('-inf')
    current_sum=0

    for num in nums:
        current_sum+=num

        max_sum=max(max_sum,current_sum)

        if current_sum<0:
            current_sum=0

    return max_sum
 
    


# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard Example
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr1}")
    print(f"Brute Force: {maxSubArray_Brute(arr1)}")
    print(f"Kadane's:    {maxSubArray_Kadane(arr1)}")
    
    print("-" * 30)
    
    # Test Case 2: All Negatives (Edge Case)
    # Kadane should return the single largest number (-1), not 0.
    arr2 = [-5, -1, -9, -2]
    print(f"Array: {arr2}")
    print(f"Kadane's:    {maxSubArray_Kadane(arr2)}")
    
    # Test Case 3: All Positives
    arr3 = [1, 2, 3, 4]
    print(f"Array: {arr3}")
    print(f"Kadane's:    {maxSubArray_Kadane(arr3)}")