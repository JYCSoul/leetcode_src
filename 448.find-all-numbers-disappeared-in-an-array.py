#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (51.13%)
# Total Accepted:    94.3K
# Total Submissions: 184.4K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for val in nums:
            i = abs(val)
            nums[i-1] = -abs(nums[i-1])
        ret = []
        for i, val in enumerate(nums):
            if val > 0:
                ret.append(i+1)
        return ret
        #  count=set()
        #  for val in nums:
        #      count.add(val)
        #  ret = []
        #  for i in range(1, len(nums)+1):
        #      if i not in count:
        #          ret.append(i)
        #  return ret
