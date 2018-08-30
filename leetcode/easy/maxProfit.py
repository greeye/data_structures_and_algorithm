'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''

def maxProfit(self,prices):
    '''
    :param self:
    :param prices:
    :return:
    '''
    flag = 0
    buy = 0
    sale = 0
    profit = 0
    for i in range(0, len(prices) - 1):
        if flag == 0 and prices[i] < prices[i + 1]:
            buy = prices[i]
            flag = 1
            continue
        if flag == 1 and prices[i] > prices[i + 1]:
            sale = prices[i]
            flag = 0
            profit = profit + (sale - buy)
    if flag == 1:
        sale = prices[len(prices) - 1]
        profit = profit + (sale - buy)

    return profit
