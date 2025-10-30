class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        print('\n')
        print(s)
        
        letters = []
        counter = []
        partitions = 1
        for letter in s:
            if letter not in letters:
                if len(letters) == k:
                    partitions += 1
                    print('', letters, '\n', counter)
                    letters = []
                    counter = []
                letters.append(letter)
                counter.append(1)
            else:
                counter[-1] += 1        


        print(partitions, letters, '\n ', counter)

        return partitions

        counter = [1]
        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                counter[-1] += 1
            else:
                counter.append(1)
        
        
        print(counter, k)

        if max(counter) == 1:
            print((len(counter))/k)
        if max(counter) == 2:
            print((len(counter)+1)/k)
        if max (counter) == 3:
            print((len(counter)+2)/k)
        return int(len(counter)/2+0.5)

        return -1
    







case1 = "accca"
k1 = 2
a1 = 3
case2 = "aabaab"
k2 = 3
a2 = 1
case3 = "xxyz"
k3 = 1
a3 = 4
case4 = "aaabbbbcccddwddccaabbccccd"
k4 = 4
a4 = 3

sol = Solution()
#print(Solution.maxPartitionsAfterOperations(sol, case1, k1) == a1)
#print(Solution.maxPartitionsAfterOperations(sol, case2, k2) == a2)
#print(Solution.maxPartitionsAfterOperations(sol, case3, k3) == a3)
print(Solution.maxPartitionsAfterOperations(sol, case4, k4) == a4)