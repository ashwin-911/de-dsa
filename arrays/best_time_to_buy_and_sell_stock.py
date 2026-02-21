"""
PROBLEM: Best Time to Buy and Sell Stock (Type I)
-------------------------------------------------
Link: Striver's SDE Sheet - Arrays
Difficulty: Easy

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5 
(Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5).

-----------------------
CONCEPTUAL LOGIC
-----------------------
1. Brute Force (Nested Loops):
   - Logic: 
     Try every possible pair of (Buy Date, Sell Date).
     For each day 'i' (Buy), look at every day 'j' after it (Sell).
     Calculate difference. Keep the max.
   - Analogy: 
     Time Travel. You go back to day 1, buy, and jump to day 2 to sell. 
     Then go back to day 1, buy, jump to day 3... very exhausting!

2. Optimal Approach (Single Pass / Dynamic Programming):
   - Logic: 
     "Buy Low, Sell High."
     As we walk through the array (days), we only need to remember one thing: 
     **"What is the lowest price I have seen SO FAR?"**
     
     If today's price is $10, and the lowest I've ever seen before today was $2, 
     then my potential profit today is $8.
     
     Algorithm:
     - Track `min_price`. Update it if we find a cheaper price.
     - Track `max_profit`. Calculate (Current Price - `min_price`). 
       If this is higher than our record, update `max_profit`.
     
   - Analogy: 
     You are walking through a market. You keep a note in your pocket of the 
     cheapest apple you've seen. Every time you see a new apple stall, you think: 
     "If I had bought the cheap apple back then and sold it here, how much would I make?"

-----------------------
COMPLEXITY ANALYSIS
-----------------------
1. Brute Force:
   - Time: O(N^2)
   - Space: O(1)

2. Optimal Approach:
   - Time: O(N) -> Single pass.
   - Space: O(1) -> Two variables.
"""

# ==========================================
# APPROACH 1: Brute Force (Nested Loops)
# ==========================================
def maxProfit_Brute(prices):
    """
    Approach 1: Brute Force
    -----------------------
    Visual Intuition:
    Check every buy-sell pair.

    Steps:
    1. Max Profit = 0.
    2. Loop i from 0 to N.
    3. Loop j from i+1 to N.
    4. Profit = prices[j] - prices[i].
    5. Update Max Profit.

    Complexity:
    - Time: O(N^2)
    - Space: O(1)
    """
    max_p = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                max_p = max(max_p, prices[j] - prices[i])
                
    return max_p






# ==========================================
# APPROACH 2: Optimal (Min Price So Far)
# ==========================================
def maxProfit_Optimal(prices):
    """
    Approach 2: Optimal (One Pass)
    ------------------------------
    Visual Intuition:
    The "Valley and Peak" Strategy.
    We want the deepest valley (min_price) that appears BEFORE the highest peak.
    
    Graph:
    |      / (Sell here!)
    |     /
    |    /
    | \_/ (Buy here!)
    
    Steps:
    1. Initialize min_price = infinity.
    2. Initialize max_profit = 0.
    3. Loop through prices:
       - Update min_price = min(min_price, current_price).
       - current_profit = current_price - min_price.
       - Update max_profit = max(max_profit, current_profit).

    Complexity:
    - Time: O(N)
    - Space: O(1)
    """
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Step 1: Update the minimum price seen so far
        if price < min_price:
            min_price = price
            
        # Step 2: Calculate profit if we sold today
        current_profit = price - min_price
        
        # Step 3: Update max profit if today is better
        if current_profit > max_profit:
            max_profit = current_profit
            
    return max_profit


def maxProfit_Optimal(prices):

    min_proce=float('inf')
    max_p=0

    for price in prices:
        if price<min_price:
            min_price=price

# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # Test Case 1: Standard
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices1}")
    print(f"Brute Force: {maxProfit_Brute(prices1)}")
    print(f"Optimal:     {maxProfit_Optimal(prices1)}")
    
    print("-" * 30)
    
    # Test Case 2: Market crash (Descending order)
    # Impossible to make profit, return 0
    prices2 = [7, 6, 4, 3, 1]
    print(f"Prices: {prices2}")
    print(f"Optimal:     {maxProfit_Optimal(prices2)}")
    
    # Test Case 3: Small dip
    prices3 = [2, 4, 1]
    # Buy at 2, Sell at 4 -> Profit 2. 
    # (Buying at 1 is useless because there is no future day to sell).
    print(f"Prices: {prices3}")
    print(f"Optimal:     {maxProfit_Optimal(prices3)}")