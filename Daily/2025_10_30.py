from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:        
        print('\n')

        n = len(target)
        print('target:', target)
        counter = [0]
        for i in range(n-1):
            diff = target[i+1]-target[i]
            if diff > 0:
                if counter[-1] >= 0:
                    counter[-1] += 1
                else:
                    counter.append(1)
            if diff < 0:
                if counter[-1] <= 0:
                    counter[-1] += -1
                else:
                    counter.append(-1) 
            if diff == 0:
                if counter[-1] < 0: 
                    counter[-1] += -1
                else:
                    counter[-1] += 1

        print('count: ', counter)

        
        if len(counter) == 1:
            if counter[0] > 0:
                return target[-1]
            if counter[0] < 0:
                return target[0]

        if counter[-1] < 0:
            counter = counter[:-1]

        if counter[0] < 0:
            operations = target[0]
        else:
            operations = 0

        index = 0
        for count in counter:
            index += abs(count)
            if count > 0:
                operations += target[index]
            elif index != counter[0]:
                operations -= target[index]
            print(count, target[index])

        print('Operations needed:', operations)
        return operations      



case1 = [1,2,3,3,3,4,5,4,3,2,3,4,5,4,3]
a1 = 8

case2 = [7,5,3,2]
a2 = 7

case3 = [2,8,4,7,3]
a3 = 11


sol = Solution()
print(Solution.minNumberOperations(sol, case1) == a1)
print(Solution.minNumberOperations(sol, case2) == a2)
print(Solution.minNumberOperations(sol, case3) == a3)