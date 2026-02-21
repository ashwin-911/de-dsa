"""
PROBLEM: Majority Element - I (> N/2 times)
-------------------------------------------
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
     Pick every element. Count its occurrences using a second loop. 
     Check if count > N/2.
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
     The "War of Attrition".
     - We maintain a 'candidate' and a 'count'.
     - If we see a number == candidate: count increases (Reinforcements).
     - If we see a number != candidate: count decreases (One-on-one combat).
     - If count hits 0: The current candidate is wiped out. The NEXT number 
       we see becomes the new candidate.
     
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
    count = 0
    candidate = None
    
    for num in nums:
        # If count is 0, we pick a new candidate
        if count == 0:
            candidate = num
        
        # If current num is same as candidate, vote +1
        if num == candidate:
            count += 1
        # If current num is different, vote -1
        else:
            count -= 1
            
    return candidate

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Array: {nums1}")
    print(f"Optimal Result: {majorityElement_Optimal(nums1)}")
    
    # Test Case 2
    nums2 = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
    print(f"Array: {nums2}")
    print(f"Optimal Result: {majorityElement_Optimal(nums2)}")