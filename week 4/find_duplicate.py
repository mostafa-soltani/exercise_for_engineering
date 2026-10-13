def find_duplicate(arr):
    seen = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen[arr[i]] = count+1

        else:
            return True
    return False


arrays = ([1, 2, 3, 1],[1, 2, 3, 4],[5, 5])


for a in arrays:
    print(find_duplicate(a))



'''
اگر حلقه اخر رو حساب نکنیم پیچیدگی زمانی میشه O(n) و اگر حلقه اخر رو حساب بکنیم بازم همون میشه و پیچیدگی فضایی یا فضای کمکی هم O(n) در بدترین شرایط چون تا اخرین رو باید در دیکشنری ذخیره بکنه 
'''