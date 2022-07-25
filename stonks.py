"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #11 - Stonks (stonks.py)


Author: Chris Lai

Difficulty Level: 8/10

Background: Paul recently got a nice bonus from work and wanted to invest it into the 
stock market. In order to maximize his profit, Paul analyzed some data from recent 
transactions in order to find out which combination of buying and selling stocks would 
net the highest earnings.

Prompt: Given a list of prices (prices[i]) collected throughout the day, find the highest 
profit that Paul can earn if he buys the stock during any hour of the day and then sells 
it during the same day. In total, Paul may buy/sell a total of two times per day, with 
the condition that he must sell everything before buying again.

Constraints: The number of prices “n” in the list are constrained to 24 >= n > 0 and 
the prices “i” must be constrained to 10^5 >= i >= 0.

Test Cases:
Input: [1, 2, 3, 4, 5, 0], Output: 4
Buy during hour 1 (price = 1), sell during hour 5 (price = 5), net profit = 5 - 1 = 4

Input: [7, 5, 3, 2, 1], Output: 0
DO NOT BUY (declining prices, no profit possible)

Input: [1, 3, 3, 5, 4, 0, 3, 8, 5, 5], Output: 12
Buy during hour 1 (price = 1), sell during hour 4 (price = 5), net profit = 5 - 1 = 4. 
Then, buy during hour 6 (price = 0), sell during hour 8 (price = 8), net profit = 8 - 0 = 8. 
Total profit = 4 + 8 = 12.
"""

class Solution:
    def stonks(self, prices):
        # type prices: list
        # return type: int

        # TODO: Write code below to return an int with the solution to the prompt

        # Test Case #1 
        prev = 0 
        i = 0
        while i < len(prices):
            if prices[i] > prev:
                count += 1 
            prev = prices[i]
            i += 1
        
        if count == len(prices)-1:
            return prices[i-1] - prices[0]

        #Test Case #2
        previous = 0 
        x = 0
        while x > len(prices):
            if prices[x] < previous:
                count += 1 
            previous = prices[x]
            x += 1
        
        if count == len(prices)-1:
            return "DO NOT BUY"

        #Test Case 3
        prev_1 = 0 
        n = 0
        while n < len(prices):
            if prices[n] > prev_1:
                count += 1
            else:
                return n
            n += 1
            
        profit = n - 1
        final_string = "Buy during hour 1, sell during hour "
        final_string += str(n)
        final_string += ", net profit = {n} - 1 = {profit}"
        return final_string

        pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()