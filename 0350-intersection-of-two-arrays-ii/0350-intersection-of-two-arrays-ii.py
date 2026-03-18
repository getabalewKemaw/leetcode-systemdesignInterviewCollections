from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res
