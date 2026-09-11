

arr = [1,2,5,0,9,4,8,5,2,4,1,5,2,3,6,2,3,2,3,6,61,64,6,6]
k = 0

arr2 = []
def check():
    seen = {}

    for index in range(len(arr)):
        item = arr[index]
        if item not in seen:
            seen[item] = index
            continue

        
        last_position = seen[item]
        seen[item] = index


        if index - last_position <= k:
            print(f'the douplicate is {last_position} and {index}')

            return True
        


    return False



print(check())
