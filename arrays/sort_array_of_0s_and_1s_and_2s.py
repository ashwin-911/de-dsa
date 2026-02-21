"""
PROBLEM: Sort an Array of 0s, 1s, and 2s
----------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order 
red (0), white (1), and blue (2).
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
Note: You must solve this problem without using the library's sort function.

Example:
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Standard Sort):
   - Logic: Use any standard sorting algorithm (Merge Sort / Quick Sort).
   - Complexity: O(N log N). This is technically a solution, but interviews 
     usually forbid it.

2. Better Approach (Counting Sort):
   - Logic: 
     Since there are only 3 distinct numbers, we can simply count them.
     Pass 1: Count how many 0s, 1s, and 2s are present.
     Pass 2: Overwrite the original array. Put 0s first, then 1s, then 2s.
   - Analogy: 
     Emptying a bucket of colored balls, counting them, and then putting them 
     back in the bucket in order.

3. Optimal Approach (Dutch National Flag Algorithm):
   - Logic: 
     We use 3 pointers to divide the array into 4 hypothetical regions:
     - [0 ... low-1]    -> All 0s (Sorted region)
     - [low ... mid-1]  -> All 1s (Sorted region)
     - [mid ... high]   -> Unsorted/Unknown region (Our workspace)
     - [high+1 ... n-1] -> All 2s (Sorted region)

     We move 'mid' through the array:
     - If arr[mid] == 0: Swap with 'low'. Increment both 'low' and 'mid'.
       (We found a 0, move it to the 0s region).
     - If arr[mid] == 1: Increment 'mid'.
       (We found a 1, it's already in the right place relative to 'low', just expand).
     - If arr[mid] == 2: Swap with 'high'. Decrement 'high'.
       (We found a 2, throw it to the back. DO NOT increment 'mid' yet, because 
       the element we swapped from the back is unknown).

   - Analogy: 
     Organizing laundry into 3 piles (White, Mixed, Dark) in a single pass. 
     You pick up an item (mid). If it's White (0), toss it left. If it's Dark (2), 
     toss it right. If it's Mixed (1), leave it in the middle.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N log N)
   - Space: O(1)

2. Better Approach (Counting):
   - Time: O(2N) -> Two passes (Count + Overwrite).
   - Space: O(1)

3. Optimal Approach (Dutch National Flag):
   - Time: O(N) -> Single pass (each element visited once).
   - Space: O(1) -> In-place swaps.
"""

# ==========================================
# APPROACH 1: Better (Counting Sort)
# ==========================================
def sortColors_Counting(arr):
    """
    Approach 1: Counting Sort
    -------------------------
    Visual Intuition:
    Count 'em up, Fill 'em in.

    Steps:
    1. Iterate and count 0s, 1s, 2s.
    2. Loop to fill 0s.
    3. Loop to fill 1s.
    4. Loop to fill 2s.

    Complexity:
    - Time: O(2N)
    - Space: O(1)
    """
    count0 = 0
    count1 = 0
    count2 = 0
    
    # Pass 1: Count frequencies
    for num in arr:
        if num == 0: count0 += 1
        elif num == 1: count1 += 1
        else: count2 += 1
        
    # Pass 2: Overwrite array
    for i in range(count0):
        arr[i] = 0
        
    for i in range(count0, count0 + count1):
        arr[i] = 1
        
    for i in range(count0 + count1, len(arr)):
        arr[i] = 2
        
    return arr
    




# ==========================================
# APPROACH 2: Optimal (Dutch National Flag)
# ==========================================
def sortColors_Optimal(arr):
    """
    Approach 2: Dutch National Flag Algorithm
    -----------------------------------------
    Visual Intuition:
    Three Pointers: Low, Mid, High.
    Mid is the Scout.
    Low is the Guard of 0s.
    High is the Guard of 2s.

    Steps:
    1. low = 0, mid = 0, high = n-1.
    2. While mid <= high:
       - If arr[mid] == 0: Swap(low, mid), low++, mid++.
       - If arr[mid] == 1: mid++.
       - If arr[mid] == 2: Swap(mid, high), high--. (Don't move mid!).

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            # Swap current element with the 0-boundary
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            
        elif arr[mid] == 1:
            # It's in the correct middle position, just move forward
            mid += 1
            
        else: # arr[mid] == 2
            # Swap current element with the 2-boundary
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # Note: We do NOT increment mid here. The element swapped 
            # from 'high' is unknown. We need to check it next iteration.
            
    return arr


def sortColors_Optimal(arr):

    low=0
    mid=0
    high=len(arr)-1

    while mid<high:

        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        
        if arr[mid]==1:
            mid+=1
        
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            ##No need to increase here as after swapping we do not know 
            ## what is at arr[mid], wether it is 0 or 1 , in next iteration it will be evaluated
            
        




# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Random mix
    arr1 = [2, 0, 2, 1, 1, 0]
    print(f"Original Array: {arr1}")
    
    # We pass a copy to Counting Sort because it modifies in-place
    res_counting = sortColors_Counting(arr1.copy())
    print(f"Counting Sort:  {res_counting}")
    
    # Optimal Sort
    sortColors_Optimal(arr1)
    print(f"Optimal Sort:   {arr1}")
    
    print("-" * 30)
    
    # Test Case 2: Already sorted
    arr2 = [0, 0, 1, 1, 2, 2]
    print(f"Original Array: {arr2}")
    sortColors_Optimal(arr2)
    print(f"Optimal Sort:   {arr2}")
    
    # Test Case 3: Reverse sorted
    arr3 = [2, 2, 1, 0, 0]
    print(f"Original Array: {arr3}")
    sortColors_Optimal(arr3)
    print(f"Optimal Sort:   {arr3}")