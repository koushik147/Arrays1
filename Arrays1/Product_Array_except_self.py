class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        for i in range(1,len(nums)):
            result.append(nums[i-1]*result[-1]) # appending nums of ith and last of array
        suffix_prod = 1 # assigning suffix product with 1
        for i in range(len(nums)-2,-1,-1):
            result[i] = result[i] * nums[i+1] * suffix_prod # multipling with suffix product
            suffix_prod *= nums[i+1]  # multiplifing suffix product with ith value
        return result # returning result