class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if total_len < 1:
            return 0
        pos = 0
        is_mid = True
        if total_len % 2 == 0:
            is_mid = False
            pos = total_len // 2 - 1
        else:
            pos = total_len // 2

        def n():
            ptr1 = ptr2 = 0
            while True:
                if ptr1 < len(nums1) and ptr2 < len(nums2):
                    if nums1[ptr1] <= nums2[ptr2]:
                        yield nums1[ptr1]
                        ptr1 += 1
                    else:
                        yield nums2[ptr2]
                        ptr2 += 1
                elif ptr1 < len(nums1):
                    yield nums1[ptr1]
                    ptr1 += 1
                elif ptr2 < len(nums2):
                    yield nums2[ptr2]
                    ptr2 += 1
                else:
                    break

        f = n()
        for i in range(pos):
            f.__next__()
        if is_mid:
            return float(f.__next__())
        else:
            return (f.__next__() + f.__next__()) / 2


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([], [15]))
