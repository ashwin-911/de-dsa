"""
PROBLEM: Find the Number that Appears Once
------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given a non-empty array of integers 'arr', every element appears twice except for one.
Find that single one.
Note: Your solution should ideally run in linear time and use constant extra space.

Example:
Input: arr = [4, 1, 2, 1, 2]
Output: 4

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Pick one number (arr[i]).
     Run a loop through the rest of the array to count how many times it appears.
     If the count is 1, that's our answer.
   - Analogy: 
     You have a pile of socks. You pick one up, then rummage through the entire 
     pile to see if you can find its match. If you can't find a match, that's 
     the missing sock.

2. Better Approach (Hashing / Frequency Map):
   - Logic: 
     Use a Dictionary (Hash Map) to store the frequency of every number.
     First pass: Count everything.
     Second pass: Check which key has a value of 1.
   - Analogy: 
     A tally sheet. You read the numbers out loud, and a friend marks a tally 
     next to each number on a whiteboard. At the end, just look for the number 
     with a single mark.

3. Optimal Approach (XOR - Bit Manipulation):
   - Logic: 
     The "Magic" Trick using XOR (^).
     Properties of XOR:
     1. A ^ A = 0 (Identical numbers kill each other).
     2. A ^ 0 = A (0 is neutral).
     3. Order doesn't matter (Associative).
     
     If we XOR every number in the array:
     [4, 1, 2, 1, 2]
     = 4 ^ (1 ^ 1) ^ (2 ^ 2)
     = 4 ^    0    ^    0
     = 4
     The duplicates cancel out to 0, leaving only the unique number.
   - Analogy: 
     Matter and Anti-matter. If two identical particles touch, they vanish 
     into nothingness. The unique particle has no partner to destroy it, so 
     it remains standing.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2) -> Double loop.
   - Space: O(1)

2. Better Approach:
   - Time: O(N) -> Two passes (Count + Check).
   - Space: O(N) -> To store the dictionary.

3. Optimal Approach:
   - Time: O(N) -> Single pass.
   - Space: O(1) -> No extra storage needed.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def getSingleElement_Brute(arr):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Pick and Search. Very slow for large arrays.

    Steps:
    1. Loop i from 0 to N.
    2. Initialize count = 0.
    3. Loop j from 0 to N.
       - If arr[j] == arr[i], increment count.
    4. If count == 1, return arr[i].

    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        num = arr[i]
        count = 0
        for j in range(n):
            if arr[j] == num:
                count += 1
        
        if count == 1:
            return num
    return -1





# ==========================================
# APPROACH 2: Better (Hashing)
# ==========================================
def getSingleElement_Better(arr):
    """
    Approach 2: Better (Dictionary)
    -------------------------------
    Visual Intuition:
    Building a Tally Sheet.

    Steps:
    1. Create an empty dictionary 'freq'.
    2. Iterate through arr. For each num, freq[num] += 1.
    3. Iterate through dictionary items.
    4. If value == 1, return the key.

    Complexity:
    - Time: O(N) (Iterate array) + O(N/2) (Iterate map) approx O(N).
    - Space: O(N/2) -> Dictionary stores unique elements.
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    for key, value in freq.items():
        if value == 1:
            return key
            
    return -1






# ==========================================
# APPROACH 3: Optimal (XOR)
# ==========================================
def getSingleElement_Optimal(arr):
    """
    Approach 3: Optimal (XOR)
    -------------------------
    Visual Intuition:
    The Survivor. 
    We smash all numbers together. Pairs vanish. The loner remains.
    
    4 ^ 1 ^ 2 ^ 1 ^ 2
    Order change -> 4 ^ (1^1) ^ (2^2)
    -> 4 ^ 0 ^ 0
    -> 4

    Steps:
    1. Initialize xor_sum = 0.
    2. Loop through every num in arr.
    3. xor_sum = xor_sum ^ num.
    4. Return xor_sum.

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    xor_sum = 0
    for num in arr:
        xor_sum = xor_sum ^ num
        
    return xor_sum




# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 1, 2, 1, 2]
    print(f"Array: {arr1}")
    print(f"Brute Force Result: {getSingleElement_Brute(arr1)}")
    print(f"Hashing Result:     {getSingleElement_Better(arr1)}")
    print(f"XOR Result:         {getSingleElement_Optimal(arr1)}")
    
    print("-" * 30)
    
    # Test Case 2 (Negative numbers work with XOR too)
    arr2 = [-1, -2, -1]
    print(f"Array: {arr2}")
    print(f"XOR Result:         {getSingleElement_Optimal(arr2)}")