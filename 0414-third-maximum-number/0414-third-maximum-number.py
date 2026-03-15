class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinict_items=set(nums)
        if len(distinict_items)<3:
            return max(distinict_items)
        else:
            return sorted(distinict_items)[-3]
        


        