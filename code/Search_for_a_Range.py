class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        if l==0:return [-1,-1]
        start=0
        end=l-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>target:end=mid-1
            elif nums[mid]<target:start=mid+1
            else:
                step=1
                left=right=mid
                while True:
                    if right+step<l and nums[right+step]==target:
                        right+=step
                        step*=2
                    else:
                        if step==1:
                            break
                        else:
                            step=1
                while True:
                    if left-step>=0 and nums[left-step]==target:
                        left-=step
                        step*=2
                    else:
                        if step==1:
                            break
                        else:
                            step=1
                return [left,right]
        return [-1,-1]
