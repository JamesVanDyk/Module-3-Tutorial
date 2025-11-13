#James Van Dyk
#array_finder.py
#finds if an item is in an array

class Solution:
    def binarysearch(self, arr, k):
        found = False
        for item in arr:
            
            if item == k:
                found = True
                return(f"Found {k} in array slot {item - 1}")
            else:
                continue
        if found != True:
            return (f"-1\n{k} not found in array")
                    
my_arr = Solution()

print(my_arr.binarysearch([1, 1, 1, 1, 2], 1))