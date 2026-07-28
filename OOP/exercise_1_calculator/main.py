from calculate import Calculation
from user_input import User_input

user_input = User_input()
calculation = Calculation()

num_1,num_2,operation = user_input.get()

print(calculation.calculate(num_1,num_2,operation))
