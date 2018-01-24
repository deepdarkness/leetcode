class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(list(set(candidates)))

        def dfs(start_index, now_list, rest_amount):
            for i in range(start_index, len(candidates)):
                if candidates[i] > rest_amount:
                    break
                elif candidates[i] == rest_amount:
                    res.append(now_list + [candidates[i]])
                    break
                else:
                    dfs(i, now_list + [candidates[i]], rest_amount - candidates[i])

        dfs(0, [], target)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([8, 7, 4, 3], 11))
