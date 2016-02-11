class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        import bisect
        l = len(nums)
        if k < 1 or t < 0 or not nums or l < 2:
            return False
        k+=1
        win=nums[:k]
        win.sort()

        for i in range(len(win)-1):
            if win[i+1]-win[i]<=t:
                return True

        for x in range(l-k):
            win.remove(nums[x])
            bisect.insort(win,nums[k+x])
            pos=bisect.bisect_left(win,nums[k+x])
            if pos>0 and win[pos]-win[pos-1]<=t:
                return True
            l=len(win)
            if pos<l-1 and win[pos+1]-win[pos]<=t:
                return True
        return False
