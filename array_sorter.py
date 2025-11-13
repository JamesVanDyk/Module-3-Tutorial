#James Van Dyk
#array_sorter.py
#sorts arrays of 0s, 1s, and 2s

class Solution:
    def sort012(self, arr):
        zeros = 0
        ones = 0
        twos = 0
        print(arr)
        for item in arr:
            if item == 0:
                zeros += 1
            elif item == 1:
                ones += 1
            else:
                twos += 1

        for i in range(zeros):
            arr[i] = 0

        for i in range(ones):
            arr[zeros + i] = 1

        for i in range(twos):
            arr[zeros + ones + i] = 2

        print(arr)
                
my_arr = Solution()

my_arr.sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])

