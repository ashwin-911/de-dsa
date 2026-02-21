"""
PROBLEM: Find the Missing Number
--------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
Given an array containing N-1 distinct numbers taken from the range 1 to N.
Find the one number that is missing from the array.

Example:
Input: N = 5, arr = [1, 2, 4, 5]
Output: 3

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Linear Search):
   - Logic: We know the numbers should be 1, 2, 3... N.
     We can pick number 1 and check if it exists in the array. Then pick 2 and check.
     The first number we can't find is the answer.
   - Analogy: Taking a roll call. You call out "Roll Number 1?" -> Present.
     "Roll Number 2?" -> Present. "Roll Number 3?" -> Silence. Found it.

2. Better Approach (Hashing / Frequency Array):
   - Logic: Create a checklist (hash map or array) of size N+1.
     Iterate through the given array and tick off the numbers present.
     Then scan the checklist to see which number has no tick.
   - Analogy: You have a guest list. As people arrive, you mark them present.
     At the end, you look at the list to see who has no checkmark.

3. Optimal Approach 1 (Summation Formula):
   - Logic: The sum of first N natural numbers is strictly (N * (N+1)) / 2.
     We calculate this Expected Sum.
     Then we calculate the Actual Sum of the array elements.
     Missing Number = Expected Sum - Actual Sum.
   - Analogy: You know the jar should weigh 50kg. It currently weighs 47kg.
     The missing stone must weigh 3kg.

4. Optimal Approach 2 (XOR - The "Engineer's Choice"):
   - Logic: XOR property: A ^ A = 0 and A ^ 0 = A.
     If we XOR all numbers from 1 to N (Expected), and XOR that result with
     all numbers in the array (Actual), all the common numbers cancel each other out (become 0).
     The only thing left remaining is the missing number.
   - Why use this over Sum? The Sum approach might cause Integer Overflow for very large N.
     XOR never overflows.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2) -> For each number 1..N, we scan the array of size N.
   - Space: O(1)

2. Better Approach:
   - Time: O(2N) -> One pass to hash, one pass to check.
   - Space: O(N) -> To store the hash map.

3. Optimal Approach (Sum & XOR):
   - Time: O(N) -> Single pass iteration.
   - Space: O(1) -> Only variables used.
"""

# ==========================================
# APPROACH 1: Brute Force (Linear Scan)
# ==========================================
def findMissingNumber_Brute(arr, N):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Checking the roll call one by one.
    
    Steps:
    1. Loop i from 1 to N.
    2. Inside, Loop j through the array to check if i exists.
    3. If flag remains False after inner loop, return i.
    
    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    for i in range(1, N + 1):
        found = False
        for num in arr:
            if num == i:
                found = True
                break
        if not found:
            return i
    return -1




# ==========================================
# APPROACH 2: Optimal 1 (Summation)
# ==========================================
def findMissingNumber_Sum(arr, N):
    """
    Approach 2: Sum Formula
    -----------------------
    Visual Intuition:
    Weighing the jar.
    Expected Weight - Actual Weight = Missing Stone.
    
    Steps:
    1. Calculate expected_sum = (N * (N + 1)) // 2.
    2. Calculate actual_sum = sum(arr).
    3. Return difference.
    
    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    expected_sum = (N * (N + 1)) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
        
    return expected_sum - actual_sum

# ==========================================
# APPROACH 3: Optimal 2 (XOR)
# ==========================================
def findMissingNumber_XOR(arr, N):
    """
    Approach 3: XOR
    ---------------
    Visual Intuition:
    The "Cancel Out" Trick.
    Imagine two decks of cards.
    Deck 1: [1, 2, 3, 4, 5]
    Deck 2: [1, 2, 4, 5] (Missing 3)
    
    If you throw both decks into a pile and pair up identical cards, 
    1 cancels 1, 2 cancels 2... 3 is left alone.
    
    XOR Logic:
    (1^2^3^4^5) ^ (1^2^4^5)
    = (1^1) ^ (2^2) ^ (4^4) ^ (5^5) ^ 3
    = 0 ^ 0 ^ 0 ^ 0 ^ 3
    = 3
    
    Steps:
    1. XOR all numbers from 1 to N (xor1).
    2. XOR all numbers in array (xor2).
    3. Return xor1 ^ xor2.
    
    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    xor1 = 0
    xor2 = 0
    
    # XOR 1 to N
    for i in range(1, N + 1):
        xor1 = xor1 ^ i
        
    # XOR Array Elements
    for num in arr:
        xor2 = xor2 ^ num
        
    return xor1 ^ xor2

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1
    N = 5
    arr = [1, 2, 4, 5]
    
    print(f"Array: {arr}, N: {N}")
    print(f"Brute Force Result: {findMissingNumber_Brute(arr, N)}")
    print(f"Sum Formula Result: {findMissingNumber_Sum(arr, N)}")
    print(f"XOR Logic Result:   {findMissingNumber_XOR(arr, N)}")
    
    print("-" * 30)
    
    # Test Case 2 (Missing the last number)
    N2 = 4
    arr2 = [1, 2, 3]
    print(f"Array: {arr2}, N: {N2}")
    print(f"XOR Logic Result:   {findMissingNumber_XOR(arr2, N2)}")