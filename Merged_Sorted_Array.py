class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Time Complexity:- O(n)
        #Space Complexity:- O(1)

        p1 = m - 1 
        p2 = n - 1
        i = m + n - 1

        while p1 >= 0 and p2 >= 0: #Continue looping until p1 and p2 are greater than 0
         if nums1[p1] >= nums2[p2]: #If value in nums1 is greater than value in nums2
            nums1[i] = nums1[p1]    #Transfer the values from nums1[p1] to nums1 at ith index
            p1 -= 1  #Decreament value of p1
         else:
            nums1[i] = nums2[p2]  #Else transfer elements from nums2[p2] to nums1 at ith index
            p2 -= 1 #Decreament value of p2
         i -= 1 #Decreament value of i

        while p2 >= 0: #Continue looping until p2 is greater than 0
          nums1[i] = nums2[p2] #Transfer all the remaining values from nums[p2] to nums1[i]
          p2 -= 1 #Decreament the value of p2
          i -= 1 #Decreament the value of i
