import ctypes



class DynamicArray:


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

    

    def append(self,value):

        if self.size == self.capacity :
            self.array = self.resize()
        
        self.array[self.size] = value


        self.size += 1

        return self.array

    def resize(self):

        self.capacity = self.capacity * 2
        
        
        arr2 = self.__create_array()
  
        arr2 = self.get_old(self.array,arr2)

        return arr2

    def get_old(self,array,new_array):
        for item in range(self.size):
            new_array[item] = array[item]
            


        return new_array


    def check_value(self,value):
        for index in range(self.size):
            item = self.array[index]
            if item == value:
                return True

        return False
            

    def get_value(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        return self.array[index]

    def get_index(self,value):
        for i in range(self.size):
            item = self.array[i]
            if item == value:
                return i

    def set_index(self,index,value):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        self.array[index] = value



    def set_value(self,value,chenge):
        for index in range(self.size):
            item = self.array[index]
            if item == value:
                self.array[index] = chenge


    def pop(self):
        item = self.array[self.size -1]

        self.array[self.size -1] = None

        self.size -= 1
        return item


    def insert(self,index,value):

        if index < 0 or index <= self.size:
            raise IndexError("index out of range")

        if self.size == self.capacity:
            self.array = self.resize()
    
        for ii in range(self.size+1,index,-1):
            self.array[ii] = self.array[ii-1]

        self.array[index] = value

        self.size += 1
        



    def delete(self,index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1
    
        
    def __str__(self):

        result = "["
        for i in range(self.size):
            result += str(self.array[i])
            if i != self.size - 1:
                result += ", "
        result += "]"
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self):
        return self.size
    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexError("index out of range")
        return self.array[key]
    def __setitem__(self, key, value):
        if key < 0 or key >= self.size:
            raise IndexError("index out of range")
        self.array[key] = value



arr = DynamicArray()

for i in range(1, 111):
    arr.append(i)

print(arr[5])

arr[5] = "hello"

print(arr[5])

print(len(arr))

arr.insert(5, 999)

print(arr)

arr.delete(5)

print(arr)

print(arr.pop())

print(len(arr))