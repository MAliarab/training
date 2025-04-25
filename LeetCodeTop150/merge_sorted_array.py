"""
Merge two sorted arrays num1, num2.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        element = None
        result_list = []
        index1 = 0
        index2 = 0

        for i in range(m + n):
            if n == 0 or index2 >= n or (index1 < m and nums1[index1] < nums2[index2]):
                element = nums1[index1]
                index1 += 1
            else:
                element = nums2[index2]
                index2 += 1

            result_list.append(element)

        for i, el in enumerate(result_list):
            nums1[i] = el

        return nums1


# Tests
print(Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(Solution().merge(nums1=[2, 0], m=1, nums2=[1], n=1))