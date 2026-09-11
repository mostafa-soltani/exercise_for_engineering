arr = [-1,-3]

maximum = 0


current = 0
for i in range(len(arr)):
    current += arr[i]

    if current < 0:
        current = 0

    if current > maximum:
        maximum = current

print(maximum)