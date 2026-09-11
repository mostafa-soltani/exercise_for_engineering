
class search:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.trys = 0
        pass

    def check_guessed_num(self,array,middle,num,start,end):
            if array[middle] < num:
                start = middle + 1
    
            elif array[middle] > num:
                end = middle - 1
    
            return start,end

    def check_value(self,array,value):
        for index in range(len(array)):
            item = array[index]
            if item == value:
                return True
            else:
                return False

            
    def binary_search(self,array,value):

        self.end = len(array) -1

        middle = (self.start + self.end) // 2

        if self.check_value(array,value):
            pass
        else:
            return None

        while array[middle] != value:
            self.trys +=1
            print(f'the number of try: {self.trys}')
            self.start,self.end = self.check_guessed_num(array,middle,value,self.start,self.end)

            middle = (self.start + self.end) // 2



        return middle



array = []

for i in range(1,100):
    array.append(i)

s = search()


print(s.binary_search(array,98))