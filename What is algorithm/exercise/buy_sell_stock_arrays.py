class sell_and_buy:
    def __init__(self,arr)-> None:
        self.arr = arr
        self.profit = 0
        self.buy_price = 0
        self.sell_price = 0
        self.holding = False
        self.b_s = {}

    def sell(self,current_price,index):

        if self.holding:
            self.sell_price = current_price
            transaction_profit = self.sell_price - self.buy_price
            self.profit += transaction_profit
            self.holding = False
            
            self.b_s[index] = ('sell',transaction_profit)

    def buy(self,current_price,index):

        if not self.holding:
            self.buy_price = current_price
            self.holding = True
            self.b_s[index] = 'buy'

    def holding_last(self,last_price,last_index):
        if self.holding:
            self.sell(last_price,last_index)
            self.b_s['whole profit'] = self.profit


    def check(self):

        for index in range(len(self.arr)-1):
            current_price = self.arr[index]
            next_price = self.arr[index+1]

            
            if current_price > next_price:
                self.sell(current_price,index)

            elif current_price < next_price:
                self.buy(current_price,index)

            
        last_index = len(self.arr) -1
        last_price = self.arr[last_index]
        self.holding_last(last_price,last_index)
            

        return self.b_s

arr = [100, 180, 260, 310, 40, 535, 695]

s_b = sell_and_buy(arr)

r = s_b.check()

print(r)