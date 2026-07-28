from minus import Minus
from add import Add
from DIvision import Division
from Multiplication import Multipilication
class Calculation:

    def __init__(self) -> None:
        self.minus = Minus()
        self.add = Add()
        self.division = Division()
        self.multipilication = Multipilication()
        pass

    def calculate(self,num_1,num_2,operation):

        if operation == '-':
            return self.minus.minus(num_1,num_2)


        if operation == '+':
            return self.add.add(num_1,num_2)

        if operation == '/':
            return self.division.division(num_1,num_2)

        if operation == '*':
            return self.multipilication.multipilication(num_1,num_2)


        else:
            print('error')
