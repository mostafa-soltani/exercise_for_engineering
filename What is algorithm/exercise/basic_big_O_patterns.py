
import ctypes

class big_O_patterns:

    def __init__(self):
        self.capacity = 4
        self.size = 0

        self.array = self.__create_array()

    def __create_array(self):
            
            array_type = self.capacity * ctypes.py_object
            
            arr = array_type()
            
            for i in range(self.capacity):
                arr[i] = None
    
            return arr

    def O_1(self,index):
        return self.array[index]

    def O_n(self):
         for item in range(self.size):
              print(self.array[item])

    def O_n_2(self):
        for x in range(self.size):
             for i in range(self.size):
                  print(x,i)

    def O_log_n(self):
        point = 20
        start = 0
        end = self.size

        for items in range(start,end):
            item = self.array[items]
            if item == point:
                print('done')

            else:
                

