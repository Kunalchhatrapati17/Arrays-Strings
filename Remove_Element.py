#Problem 27 of leetcode
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Time complexity= O(N)
        #Space Complexity=O(1)

        l=0 #It keeps the count of values which are not equal to val
        for i in range(len(nums)): #Loop till the end of the list
           if nums[i]!=val: # If nums[i]!=val
             nums[l]=nums[i] # Transfer the value at ith location
             l+=1 #Increament the value of l
        return l #Return the count of l
