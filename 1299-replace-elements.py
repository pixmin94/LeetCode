# Given an array arr, replace every element in that array with the greatest element among 
# the elements to its right, and replace the last element with -1.

# After doing so, return the array.

# O(n^2):
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         for index,var in enumerate(arr):
#             newarr = arr[index+1:]
#             if len(newarr) == 0:
#                 arr[index] = -1
#             else:
#                 arr[index] = max(newarr)
#         return arr

# O(n):
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

