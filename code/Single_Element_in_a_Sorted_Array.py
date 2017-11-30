class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = nums[0]
        switch = True
        for i in nums[1:]:
            if switch:
                if i == p:
                    switch = False
                else:
                    return p
            else:
                p = i
                switch = True
        return nums[-1]
