from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

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
        
        # catch the case that is always true, as it is not caught it the general case        
        if k == 1:
            return True
        
        # if any sequence of striclty increasing numbers is longer than both subarrays it is true
        if any(seq >= (k*2-1) for seq in count) :
            return True
        
        # if two sequences of strictly increasing numbers longer than k are only seperated by one 
        # not strictly increasing pair it is still valid
        for i in range(len(count)-2):
            if ((count[i] >= k-1) and 
                (count[i+1] == -1) and 
                (count[i+2] >= k-1)):
                return True
        
        return False

case1 = [2,5,7,8,9,2,3,4,3,1]
k1 = 3

case2 = [1,2,3,4,4,4,4,5,6,7]
k2 = 5

case3 = [1,2,3,4,4,4,4,5,6,7]
k3 = 2

case4 = [1,2]
k4 = 1

sol = Solution()
print(Solution.hasIncreasingSubarrays(sol, case1, k1)==True)
print(Solution.hasIncreasingSubarrays(sol, case2, k2)==False)
print(Solution.hasIncreasingSubarrays(sol, case3, k3)==True)
print(Solution.hasIncreasingSubarrays(sol, case4, k4)==True)