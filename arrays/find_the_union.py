"""
PROBLEM: Find the Union of Two Sorted Arrays
--------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Medium

Problem Statement:
Given two sorted arrays, arr1 and arr2 of size N and M respectively, return the 
Union of the two arrays.
The Union of two arrays can be defined as the common and distinct elements 
in the two arrays. The elements in the union should be in ascending order.

Example:
Input: arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 3]
Output: [1, 2, 3, 4, 5]

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Using Set):
   - Logic: 
     A Set data structure inherently stores unique elements. 
     We can simply insert every element from both arrays into a Set.
     Since the Set might destroy the order, we sort the result at the end.
   - Analogy: 
     Dumping two buckets of Lego bricks into one big box. The box automatically 
     removes duplicates. Then you arrange them by size.

2. Optimal Approach (Two Pointers):
   - Logic: 
     Since the arrays are ALREADY sorted, we can use the "Zipper" technique.
     We compare the 'heads' of both arrays.
     - If arr1's head is smaller, it goes into the Union first.
     - If arr2's head is smaller, it goes in.
     - If they are equal, pick one (it doesn't matter) and advance BOTH pointers 
       (to avoid adding the duplicate twice).
     
     *Crucial Step*: Before adding ANY number to our Union list, we check if 
     it's the same as the last number we added. If yes, we skip it to ensure uniqueness.
   - Analogy: 
     Two lines of students arranged by height. You are the teacher picking them 
     to enter a room. You look at the front of both lines and pick the shorter 
     student to go in first. If twins are at the front of both lines, you send 
     one in and tell the other to go home.

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O( (N+M)log(N+M) ) -> Inserting is cheap, but Sorting the final set takes log time.
   - Space: O(N+M) -> To store the set.

2. Optimal Approach:
   - Time: O(N+M) -> We traverse both arrays exactly once.
   - Space: O(1) -> If we don't count the space used for the returned list (Auxiliary Space).
"""

# ==========================================
# APPROACH 1: Brute Force (Using Set)
# ==========================================
def findUnion_Brute(arr1, arr2):
    """
    Approach 1: Brute Force (Set)
    -----------------------------
    Visual Intuition:
    Collect everything, Filter duplicates, Sort.

    Steps:
    1. Create a Set.
    2. Add all elements of arr1 to Set.
    3. Add all elements of arr2 to Set.
    4. Convert Set to List and Sort it.
    5. Return List.

    Complexity:
    - Time: O( (N+M) * log(N+M) )
    - Space: O(N+M)
    """
    # Using a set to handle duplicates automatically
    s = set()
    
    for num in arr1:
        s.add(num)
        
    for num in arr2:
        s.add(num)
        
    # Convert back to sorted list
    union_arr = sorted(list(s))
    
    return union_arr



    



# ==========================================
# APPROACH 2: Optimal (Two Pointers)
# ==========================================
def findUnion_Optimal(arr1, arr2):
    """
    Approach 2: Optimal (Two Pointers / Zipper Merge)
    -------------------------------------------------
    Visual Intuition:
    Merging two sorted traffic lanes into one.
    - Pointer i tracks arr1.
    - Pointer j tracks arr2.
    - We always pick the smaller value to maintain sorted order.
    - We always check 'union[-1]' to avoid duplicates.

    Steps:
    1. Initialize i=0, j=0, union=[]
    2. Loop while i < N and j < M:
       - Compare arr1[i] and arr2[j].
       - If arr1[i] <= arr2[j]: 
         Check if union is empty OR union[-1] != arr1[i]. If true, append arr1[i].
         Increment i.
       - If arr2[j] < arr1[i]: 
         Check if union is empty OR union[-1] != arr2[j]. If true, append arr2[j].
         Increment j.
    3. After loop, one array might have leftovers. Repeat the add-check logic for 
       remaining elements of arr1 and arr2.

    Complexity:
    - Time: O(N + M)
    - Space: O(1) (Auxiliary)
    """
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    union_arr = []
    
    while i < n and j < m:
        # Case 1: arr1 element is smaller or equal
        if arr1[i] <= arr2[j]:
            # Add ONLY if union is empty OR it's not a duplicate of the last added
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
            
        # Case 2: arr2 element is smaller
        else:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
            
    # Consume remaining elements from arr1
    while i < n:
        if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
        
    # Consume remaining elements from arr2
    while j < m:
        if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
        
    return union_arr








# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 3, 4, 4, 5, 6]
    print(f"Array 1: {a1}")
    print(f"Array 2: {a2}")
    
    print(f"Brute Force Union: {findUnion_Brute(a1, a2)}")
    print(f"Optimal Union:     {findUnion_Optimal(a1, a2)}")
    
    print("-" * 30)
    
    # Test Case 2: Disjoint Arrays
    b1 = [1, 2]
    b2 = [3, 4]
    print(f"Array 1: {b1}")
    print(f"Array 2: {b2}")
    print(f"Optimal Union: {findUnion_Optimal(b1, b2)}")
    
    print("-" * 30)

    # Test Case 3: Duplicates inside source arrays
    c1 = [1, 1, 1, 2]
    c2 = [2, 2, 3, 3]
    # Expected: [1, 2, 3]
    print(f"Array 1: {c1}")
    print(f"Array 2: {c2}")
    print(f"Optimal Union: {findUnion_Optimal(c1, c2)}")