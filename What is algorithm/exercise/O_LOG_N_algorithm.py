
class game:

    def __init__(self) -> None:
        self.capacity = 6
        self.size = 0
        self.trys = 0
        self.start = 0
        self.end = int('1000000000',base=10)
        


    def ask_user(self):
        print(f'hello. please inter what you consider is the number in between {self.start} to {self.end}')

        num = int(input(''))

        return num

    def check_guessed_num(self,g_num,num,start,end):
        if g_num < num:
            start = g_num + 1

        elif g_num > num:
            end = g_num - 1

        return start,end
        

    def guess(self,num : int):

        middle = (self.start+self.end) //2
        while middle != num:
            self.trys += 1
            print(f'the number of trys is :{self.trys}')
            self.start,self.end = self.check_guessed_num(middle,num,self.start,self.end)
            middle = (self.start+self.end)//2

        print('find your number.',num)


    def start_(self):

        num = self.ask_user()

        self.guess(num)

        print(f'the number of trys is :{self.trys}')



ie = game()

ie.start_()