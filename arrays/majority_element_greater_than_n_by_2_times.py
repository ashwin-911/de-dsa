"""
PROBLEM: Majority Element (> N/2 times)
---------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy/Medium

Problem Statement:
Given an array 'nums' of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2 
(Length is 7. Majority requires > 3.5. '2' appears 4 times).

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Pick every element. Count its occurrences. Check if count > N/2.
   - Analogy: 
     Asking every single person in a room "Are you the leader?" and then asking 
     everyone else "Is he the leader?". Very slow.

2. Better Approach (Hashing / Map):
   - Logic: 
     Count frequencies of all elements using a Dictionary.
     Then iterate through the dictionary to find which key has value > N/2.
   - Analogy: 
     Ballot Box. Everyone casts a vote. You count the votes at the end.

3. Optimal Approach (Boyer-Moore Voting Algorithm):
   - Logic: 
     The "Battlefield" Strategy.
     - We maintain a 'candidate' and a 'count'.
     - If we see a number == candidate: count increases (Reinforcements arrive).
     - If we see a number != candidate: count decreases (One-on-one combat, both die).
     - If count hits 0: The current candidate is wiped out. The NEXT number we see 
       becomes the new candidate.
     
     Why it works: 
     Since the Majority Element appears > N/2 times, it has more soldiers than 
     ALL other elements combined. Even if they fight 1-vs-1 against everyone else, 
     the Majority faction will still have soldiers left standing at the end.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2)
   - Space: O(1)

2. Better Approach (Hashing):
   - Time: O(N) -> Two passes (Count + Check).
   - Space: O(N) -> To store the map.

3. Optimal Approach (Boyer-Moore):
   - Time: O(N) -> Single pass.
   - Space: O(1) -> Only 2 variables used.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def majorityElement_Brute(nums):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Pick and Count.

    Steps:
    1. Loop i through nums.
    2. Reset count = 0.
    3. Loop j through nums.
       - If nums[j] == nums[i], count++.
    4. If count > n/2, return nums[i].

    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        
        if count > n // 2:
            return nums[i]
            
    return -1






# ==========================================
# APPROACH 2: Better (Hashing)
# ==========================================
def majorityElement_Better(nums):
    """
    Approach 2: Hashing
    -------------------
    Visual Intuition:
    The Tally Sheet.

    Steps:
    1. Create 'freq' dict.
    2. Count occurrences of each num.
    3. Iterate through dict. If val > n/2, return key.

    Complexity:
    - Time: O(N)
    - Space: O(N)
    """
    n = len(nums)
    freq = {}
    
    # Pass 1: Count
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
    # Pass 2: Check
    for key, value in freq.items():
        if value > n // 2:
            return key
            
    return -1

# ==========================================
# APPROACH 3: Optimal (Boyer-Moore Voting)
# ==========================================
def majorityElement_Optimal(nums):
    """
    Approach 3: Boyer-Moore Voting Algorithm
    ----------------------------------------
    Visual Intuition:
    King of the Hill.
    - Candidate: The current King.
    - Count: The King's Health/Army size.
    
    If you meet an ally (same number), Army grows (+1).
    If you meet an enemy (different number), Army shrinks (-1).
    If Army dies (0), the next person you see claims the throne.

    Steps:
    1. Init count = 0, candidate = None.
    2. Loop through nums:
       - If count == 0: candidate = num.
       - If num == candidate: count += 1.
       - Else: count -= 1.
    3. Return candidate.
    (Note: Since problem guarantees majority exists, we don't need a verification pass).

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate


def majorityElement_Optimal(nums):

    count=0
    candidate=None

    for num in nums:

        if count==0:
            candidate=num

        if num==candidate:
            count+=1
        else:
            count-=1
    
    return candidate



# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Array: {nums1}")
    print(f"Brute Force: {majorityElement_Brute(nums1)}")
    print(f"Hashing:     {majorityElement_Better(nums1)}")
    print(f"Boyer-Moore: {majorityElement_Optimal(nums1)}")
    
    print("-" * 30)
    
    # Test Case 2: All same
    nums2 = [5, 5, 5]
    print(f"Array: {nums2}")
    print(f"Boyer-Moore: {majorityElement_Optimal(nums2)}")
    
    # Test Case 3: Mixed
    nums3 = [3, 3, 4]
    print(f"Array: {nums3}")
    print(f"Boyer-Moore: {majorityElement_Optimal(nums3)}")