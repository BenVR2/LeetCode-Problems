from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        print('\n\n')
        
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i) 
        
        possibleSolutions = 0
        for zero in zeros:
            a = sum(nums[:zero])
            b = sum(nums[zero:])
            print(zero, a, b)       
            if abs(a-b) <= 1:
                possibleSolutions += 1    


        return possibleSolutions

        nums_bu = nums * 1
        n = len(nums)
        
        for zero in zeros:
            print('\n\n')
            direction = +1
            index = zero + direction
            nums = nums_bu * 1
            print(nums)
            while 0 <= index <= n-1:
                if nums[index] == 0:
                    index = index + direction
                elif nums[index] > 0:
                    nums[index] -= 1
                    print(nums)
                    direction *= -1
                    index = index + direction


        print('\n\n')
        return None




case1 = [1,0,2,0,3]
a1 = 1

sol = Solution()
print(Solution.countValidSelections(sol, case1) == a1)
