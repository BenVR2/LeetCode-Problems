from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        # calculate n - n+1, for strictly increasing this should be < 0
        diff = []
        for i in range(len(nums)-1):
            diff.append((nums[i]-nums[i+1]) < 0)

        # count the occurences of strictly increasing values
        count = [0]
        for i in range(len(diff)):
            if diff[i] == True:
                if count[-1] < 0:
                    count.append(1)
                else:
                    count[-1] += 1
            else:
                if count[-1] > 0:
                    count.append(-1)
                else:
                    count[-1] += -1
        
        print(count)

        # catch the special case
        if len(nums) == 2 or len(nums) == 3:
            return 1
        

        sequenceLenghts = [0]

        # take longest sequence of strictly increasing numbers and divide into two sequences
        sequenceLenghts.append(int((max(count)+1)/2))

        # if there are two adjecent sequences of striclty increasing numbers 
        # take the smaller sequence as maximum length
        for i in range(len(count)-2):
            if count[i+1] == -1:
                sequenceLenghts.append(int(min(count[i], count[i+2])+1))
        
        

        # return the max of the options
        return max(sequenceLenghts)


case1 = [2,5,7,8,9,2,3,4,3,1]
k1 = 3

case2 = [1,2,3,4,4,4,4,5,6,7]
k2 = 2

case3 = [1,2,3,4,4,4,4,5,6,7]
k3 = 2

case4 = [5,2]
k4 = 1

case5 = [20,-2,-18]
k5 = 1

case6 = [6,9,15,-5,5,14,-14,10]
k6 = 3

sol = Solution()
print(Solution.maxIncreasingSubarrays(sol, case1) == k1)
print(Solution.maxIncreasingSubarrays(sol, case2) == k2)
print(Solution.maxIncreasingSubarrays(sol, case3) == k3)
print(Solution.maxIncreasingSubarrays(sol, case4) == k4)
print(Solution.maxIncreasingSubarrays(sol, case5) == k5)
print(Solution.maxIncreasingSubarrays(sol, case6) == k6)