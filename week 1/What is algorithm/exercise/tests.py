class distanse_within_k:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}

    def find(self,user_distance):

        for i in range(len(self.arr)):

            if self.arr[i] in self.seen:
                distance = i - self.seen[self.arr[i]]

                if distance <= user_distance:
        
                    return 'yes'

            self.seen[self.arr[i]] = i
            
                
        return 'no'

class rearrage_array_even_is_greater_odd:
    def __init__(self,arr) -> None:
        self.arr = arr

    def rearrange(self):
        for i in range(len(self.arr)):
            if i % 2 == 0:
                if self.arr[i] <= self.arr[i-1]:
                    continue
                else:
                    hold = self.arr[i-1]
                    self.arr[i-1] = self.arr[i]
                    self.arr[i] = hold

            if i % 2 != 0:
                if self.arr[i] >= self.arr[i-1]:
                    continue
                else:
                    hold = self.arr[i-1]
                    self.arr[i-1] = self.arr[i]
                    self.arr[i] = hold

        return self.arr

class sum_of_all_sub_arrays:
    def __init__(self,arr) -> None:
        self.arr = arr

    def sum(self):
        sum = 0

        for i in range(len(self.arr)):
            temp = 0

            for n in range(i,len(self.arr)):
                temp += self.arr[n]

                sum += temp

        return sum

class buy_sell:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.profit = 0

    def show(self):
        results = {}
        buy = False
        n = len(self.arr) -1

        for i in range(n):
            if self.arr[i] < self.arr[i+1] and buy == False:
                results[self.arr[i]] = 'buy'
                buy = True
                self.profit += self.arr[i]

            elif self.arr[i] > self.arr[i+1] and buy == True:
                results[self.arr[i]] = 'sell'
                buy = False

        if buy == True:
            results[self.arr[n]] = 'sell'

        return results,self.profit

class unique_num:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}
        self.count = 1

    def find(self):
        for i in range(len(self.arr)):
            if self.arr[i] in self.seen:
                self.seen[self.arr[i]] = self.count +1

            if self.arr[i] not in self.seen:
                self.seen[self.arr[i]] = self.count

        for ii,count in self.seen.items():
            if count == 1:
                return ii

        return -1

class find_missing_num:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}
        self.count = 1
        self.biggest = 0

    def find(self):
        for i in range(len(self.arr)):
            self.seen[self.arr[i]] = True

        for value in range(1,len(self.arr)+2):

            if value not in self.seen:
                return value

            else:
                continue
            
class find_missing_duplicate:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}
        self.count = 1
        self.results = []

    def find(self):
        for i in range(len(self.arr)):
            if self.arr[i] not in self.seen:
                self.seen[self.arr[i]] = self.count
            else:
                self.seen[self.arr[i]] = self.count +1

        for ii in range(len(self.arr)):
            if self.seen[self.arr[ii]] == 2:
                if self.arr[ii] not in self.results:
                    self.results.append(self.arr[ii])

        for iii in range(1,len(self.arr)):
            if iii not in self.seen:
                self.results.append(iii)

            else:
                pass



        return self.results

class only_repeating_1_to_n_1:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}
        self.count = 1
        

    def find(self):
        for i in range(len(self.arr)):
            if self.arr[i] not in self.seen:
                self.seen[self.arr[i]] = self.count
            else:
                self.seen[self.arr[i]] = self.count+1

        for num,count in self.seen.items():
            if count >= 2:
                return num

class sorted_subsequence_of3:
    def __init__(self,arr) -> None:
        self.arr = arr
        # this lines make an fake number of infinite that is bigger that every number
        self.first = float('inf')
        self.second = float('inf')
        self.prevfirst = float('inf')

    def find(self):
        # the length of arr
        n = len(self.arr)

        # the loop for arr
        for index in range(n):
            # current value in arr
            x = self.arr[index]
            # find the first small number 
            if x <= self.first:
                self.first = x
            # find the decond or middle number
            elif x <= self.second:
                self.second = x
                # save the first number if still a smaller exists after it
                self.prevfirst = self.first

            else:
                # return the sequence
                return [self.prevfirst,self.second,x]

        # if nothinf found return this
        return []   

class kadanes_algorithm:
    def __init__(self,arr) -> None:
        self.arr = arr

    def find(self):
        result = self.arr[0]

        maxEnding = self.arr[0]

        for i in range(1,len(self.arr)):

            maxEnding = max(maxEnding + self.arr[i],self.arr[i])

            result = max(maxEnding,result)

        return result

class equilibrium_index:
    def __init__(self,arr) -> None:
        self.arr = arr

    def summ(self):
        sum = 0
        for index in range(len(self.arr)):
            sum += self.arr[index]

        return sum

    def start(self):
        left = 0
        right = 0
        current = 0
        total = self.summ()

        for index in range(len(self.arr)):
            current = self.arr[index]

            right = total - left - current

            if left == right:
                return index

            left += current

        return -1

class split_arrays_into_3_equal:
    def __init__(self,arr) -> None:
        self.arr = arr

    def summ(self):
        sum = 0
        for index in range(len(self.arr)):
            sum += self.arr[index]

        return sum

    def get(self):
        point = []
        c_sum = 0
        total = self.summ()

        if not total // 3 != 0:
            point = [-1,-1]

        target = total / 3

        for index in range(len(self.arr)):
            c_sum += self.arr[index]

            if c_sum == target:
                point.append(index)
                c_sum = 0
                if len(point) == 2:
                    return point

            else:
                continue

        point = [-1,-1]
        return point
            


if __name__ == '__main__':


    d_w_k_arr = [1, 2, 3, 1, 4, 5]

    d_w_k= distanse_within_k(d_w_k_arr)

    print(f'distance_within_k arr {d_w_k_arr}')
    print('distance_within_k result',d_w_k.find(3))
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')

    r_a_e_i_g_o_arr = [1,2,2,1]

    r_a_e_i_g_o = rearrage_array_even_is_greater_odd(r_a_e_i_g_o_arr)

    print(f'rearrage_array_even_is_greater_odd arr {r_a_e_i_g_o_arr}')
    print('rearrage_array_even_is_greater_odd result',r_a_e_i_g_o.rearrange())
    print('time comlexity = O(n) - space complexity = O(n)')

    print('-----------------------------------------------------------------------')


    s_o_a_s_arr = [1,2,3,4]

    s_o_a_s = sum_of_all_sub_arrays(s_o_a_s_arr)

    print(f'sum_of_all_sub_arrays arr {s_o_a_s_arr}')
    print('sum_of_all_sub_arrays result',s_o_a_s.sum())
    print('time comlexity = O(n^2) - space complexity = O(1)')

    print('-----------------------------------------------------------------------')


    b_s_arr = [100, 180, 260, 310, 40, 535, 695]

    b_s = buy_sell(b_s_arr)

    print(f'buy and sell arr {b_s_arr}')
    print('buy and sell result',b_s.show())
    print('time comlexity = O(n) - space complexity = O(1)')

    print('-----------------------------------------------------------------------')


    U_n_arr = [2,2, 3, 5, 4, 5, 4]


    u_n = unique_num(U_n_arr)

    print(f'unique number arr {U_n_arr}')
    print('unique number result',u_n.find())
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    f_m_n_arr = [8, 2, 4, 5, 3, 7, 1]

    f_m_n = find_missing_num(f_m_n_arr)

    print(f'find the missing number arr {f_m_n_arr}')
    print('unique number result',f_m_n.find())
    print('time comlexity = O(n2) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    f_m_d_n_arr = [3,1,3]

    f_m_d_n = find_missing_duplicate(f_m_d_n_arr)

    print(f'find the missing and duplicate number arr {f_m_d_n_arr}')
    print('find the missing and duplicate number result',f_m_d_n.find())
    print('time comlexity = O(n2) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    o_r_f_1_arr = [1, 3, 2, 3, 4]

    o_r_f_1 = only_repeating_1_to_n_1(o_r_f_1_arr)

    print(f'only repeating number from 1 to n-1  arr {o_r_f_1_arr}')
    print('only repeating number from 1 to n-1 result',o_r_f_1.find())
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    s_s_3_arr = [12, 11, 10, 5, 6, 2, 30]

    s_s_3 = sorted_subsequence_of3(s_s_3_arr)

    print(f'sorted sequence of 3 arr {s_s_3_arr}')
    print('sorted sequence of 3 result',s_s_3.find())
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    kadanes_arr = [-2,-3]
    
    kadanes = kadanes_algorithm(kadanes_arr)

    print(f'kadanes algorithm arr {kadanes_arr}')
    print('kadanes algorithm result',kadanes.find())
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    e_i_arr = [1,2,0,3]
    
    e_i = equilibrium_index(e_i_arr)

    print(f'equilibrium index arr {e_i_arr}')
    print('equilibrium index result',e_i.start())
    print('time comlexity = O(n) - space complexity = O(1)')


    print('-----------------------------------------------------------------------')


    s_a_i_3_arr = [1, 3, 4, 0, 4]
    
    s_a_i_3 = split_arrays_into_3_equal(s_a_i_3_arr)

    print(f'split_arrays_into_3_equal arr {s_a_i_3_arr}')
    print('split_arrays_into_3_equal result',s_a_i_3.get())
    print('time comlexity = O(n) - space complexity = O(1)')