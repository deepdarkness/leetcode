class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        container = path.split('/')
        simple_list = []
        for i in container:
            if not i or i == '':
                continue
            if i == '.':
                continue
            elif i == '..':
                simple_list = simple_list[:-1]
            else:
                simple_list.append(i)
        res = ''
        for k in simple_list:
            res += ('/' + k)
        return res
