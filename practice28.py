def find_best_days(prices):
    n = len(prices)
    min_price = prices[0]
    min_day = 1
    best_profit = 0
    buy_day = -1
    sell_day = -1
    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > best_profit:
            best_profit = profit
            buy_day = min_day
            sell_day = i + 1
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i + 1
    if best_profit == 0:
        return None
    return buy_day, sell_day, best_profit

prices = list(map(int, input().split()))
result = find_best_days(prices)
if result is None:
    print("перепродажа с прибылью невозможна")
else:
    buy_day, sell_day, profit = result
    print("покупать в день", buy_day)
    print("продавать в день", sell_day)
    print("прибыль с одной акции:", profit)
    print("прибыль за 1000 акций:", profit * 1000)