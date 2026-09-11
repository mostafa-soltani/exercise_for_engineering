arr = [1,2,3,4]

total_sum = 0
current_sub_array_sum = 0
for index_start in range(len(arr)):
    current_sub_array_sum = 0
    for index in range(index_start,len(arr)):
        current_sub_array_sum += arr[index]


        total_sum += current_sub_array_sum


print(total_sum)