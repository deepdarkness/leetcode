
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        student_amount = len(M)

        circle_amount = 0
        circle_tag = [0]*student_amount
        dig_cache = []

        def friendsOfStudentN(N):
            friendsList = []
            for ptr in xrange(0, student_amount):
                if M[N][ptr] == 1:
                    friendsList.append(ptr)
            return friendsList

        def digFriends(stu_ptr):
            if stu_ptr in dig_cache:
                return
            dig_cache.append(stu_ptr)
            for p in friendsOfStudentN(stu_ptr):
                circle_tag[p] = 1
                digFriends(p)
        
        for sptr in xrange(0, student_amount):
            if circle_tag[sptr] == 0:
                circle_amount += 1
                digFriends(sptr)
        
        return circle_amount


if __name__ == '__main__':
    slu = Solution()
    M=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(slu.findCircleNum(M))