prices = [7, 1, 5, 3, 6, 4]
buy_stock = prices[0]
maxi = 0
for i in range(1, len(prices)):
    if prices[i] < buy_stock:
        buy_stock = prices[i]
    else:
        # price is greater and we can sell the stock
        maxi = max(prices[i] - buy_stock, maxi)
print(maxi)