def find_number_by_1_reapeted_count(arr):

    seen = {}

    for i in range(len(arr)):

        if arr[i] not in seen:
            seen[arr[i]] = 1

        else:
            seen[arr[i]] += 1

    for item,cc in seen.items():
        if cc == 1:
            return item

    return None


a = ([1,2,4,1,1,5,6,9,8,7,7,8,9,6,5,2,3,9],[1,2,3,4,5,6,7,8,9,9,8,7,5,4,3,2,1])

for i in a:
    print(find_number_by_1_reapeted_count(i))