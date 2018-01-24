class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        while True:
            if candidates[-1] > target:
                candidates = candidates[:-1]
            else:
                break
        if not candidates:
            return res

        def dfs(start_index, now_list, rest):
            for i in range(start_index, len(candidates)):
                if candidates[i] > rest:
                    break
                elif candidates[i] == rest:
                    ix = tuple(now_list + [candidates[i]])
                    if ix not in res:
                        res.append(ix)
                else:
                    dfs(i + 1, now_list + [candidates[i]], rest - candidates[i])

        dfs(0, [], target)
        return [list(x) for x in res]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
