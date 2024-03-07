class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Time Complexity:- O(n)
        # Space Complexity:- O(n)
        n = len(nums)
        result = [1] * n  # Initialize result list with all elements as 1
        left_product = 1
        
        # Calculate product of elements to the left of current element
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        
        # Calculate product of elements to the right of current element and multiply with the already computed product
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
         
        return result
