class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        days = 1
        while self.stock and price >= self.stock[-1][0]:
            days += self.stock[-1][1]
            self.stock.pop()
        self.stock.append((price, days))
        return days
            


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)