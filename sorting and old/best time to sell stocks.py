#  function definationn
#  time complexity O(n)

def findMaxProfit(price):
    minPrice = float('inf')
    maxprofit = 0
    
    for i in range (len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxprofit:
            maxprofit = price[i] - minPrice
    return maxprofit
              


# driver code

price = [7,1,5,3,6,4]
maxProfitValue = findMaxProfit(price);
print("the maximum profit of buying and selling the stocks is :", maxProfitValue);