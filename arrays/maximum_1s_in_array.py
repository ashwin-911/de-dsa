"""
PROBLEM: Maximum Consecutive Ones
---------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given a binary array 'nums' (containing only 0s and 1s), return the maximum number 
of consecutive 1s in the array.

Example:
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3 (The first two 1s are consecutive, but the last three 1s are more)

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     For every single '1' we find, we launch a search to see how far the 
     streak goes.
     "Start a streak at index 0... length 2."
     "Start a streak at index 1... length 1."
     "Start a streak at index 3... length 3."
   - Analogy: 
     You are looking for the longest traffic jam. You stop at every single car 
     and count how many cars are in front of it before a gap appears. 
     Very repetitive!

2. Optimal Approach (Single Pass):
   - Logic: 
     We iterate through the array once. We keep a running counter ('current_count').
     - If we see a 1: Increment the counter. Update the 'max_count' record if 
       current is higher.
     - If we see a 0: The streak is broken! Reset 'current_count' to 0 immediately.
   - Analogy: 
     You are running a race. Every step you take (seeing a 1) adds to your speed. 
     If you trip (seeing a 0), you lose all momentum and have to start from 
     speed 0 again. You just remember your "top speed" recorded during the run.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2) -> Worst case (all 1s), we re-count the same ones repeatedly.
   - Space: O(1)

2. Optimal Approach:
   - Time: O(N) -> Single pass traversal.
   - Space: O(1) -> Only 2 variables (count, max).
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def findMaxConsecutiveOnes_Brute(nums):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Checking every possible starting point for a streak.

    Steps:
    1. Initialize max_count = 0.
    2. Loop i from 0 to N.
    3. Reset current_count = 0.
    4. Loop j from i to N.
       - If nums[j] == 1, increment current_count.
       - If nums[j] == 0, BREAK immediately (streak broken).
    5. Update max_count.
    
    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    max_count = 0
    n = len(nums)
    
    for i in range(n):
        current_count = 0
        for j in range(i, n):
            if nums[j] == 1:
                current_count += 1
            else:
                break
        max_count = max(max_count, current_count)
        
    return max_count








# ==========================================
# APPROACH 2: Optimal (Single Pass)
# ==========================================
def findMaxConsecutiveOnes_Optimal(nums):
    """
    Approach 2: Optimal
    -------------------
    Visual Intuition:
    The "Heartbeat" Monitor. 
    It goes up, up, up... (1, 1, 1). 
    Flatlines to zero (0). 
    Starts going up again... (1, 1).

    Steps:
    1. Initialize max_cnt = 0, cnt = 0.
    2. Iterate through nums.
    3. If nums[i] == 1:
       - cnt += 1
       - max_cnt = max(max_cnt, cnt)
    4. Else (nums[i] == 0):
       - cnt = 0 (Reset streak)
    5. Return max_cnt.

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    max_cnt = 0
    cnt = 0
    
    for num in nums:
        if num == 1:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
            
    return max_cnt


def findMaxConsecutiveOnes_Optimal(nums):
     
     max_count=0
     current_count=0

     for num in nums:
        if num==1:
            current_count+=1
            max_count=max(max_count,current_count)
        else:
            current_count=0
    
    return max_count






# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Mixed 0s and 1s
    nums1 = [1, 1, 0, 1, 1, 1]
    print(f"Array: {nums1}")
    print(f"Brute Result:   {findMaxConsecutiveOnes_Brute(nums1)}")
    print(f"Optimal Result: {findMaxConsecutiveOnes_Optimal(nums1)}")
    
    print("-" * 30)
    
    # Test Case 2: All 1s
    nums2 = [1, 1, 1, 1]
    print(f"Array: {nums2}")
    print(f"Optimal Result: {findMaxConsecutiveOnes_Optimal(nums2)}")
    
    # Test Case 3: All 0s
    nums3 = [0, 0, 0]
    print(f"Array: {nums3}")
    print(f"Optimal Result: {findMaxConsecutiveOnes_Optimal(nums3)}")