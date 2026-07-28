


class User_input:

    def __init__(self) -> None:
        pass

    def get(self)-> tuple:
        print('input of number 1:')
        num_1 = float(input(""))

        print('input of number 2: ')

        num_2 = float(input(''))

        print('what operation do you want')
        print('/  -   =   *')

        operation = str(input(''))

        return num_1, num_2,operation