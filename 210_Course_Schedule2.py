from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites == []:
            return [i for i in range(0, numCourses)]
        self.n = numCourses
        courseOrder = []
        AOV, indegreeHash = self.getAOVandIndegree(prerequisites)
        initCourses = [initCourse for initCourse in indegreeHash if indegreeHash[initCourse]==0]
        queue = deque(initCourses)
        while queue:
            curCourse = queue.popleft()
            courseOrder.append(curCourse)
            del indegreeHash[curCourse]
            for neighbor in AOV[curCourse]:
                indegreeHash[neighbor] -= 1 
                if indegreeHash[neighbor] == 0:
                    queue.append(neighbor)
        if len(indegreeHash) > 0 :
            return []
        return courseOrder
    
    def getAOVandIndegree(self, prerequisites):
        AOV = {x:[] for x in range(self.n)}
        indegreeHash = {x: 0 for x in range(self.n)}
        for coursePair in prerequisites:
            AOV[coursePair[1]].append(coursePair[0])
            indegreeHash[coursePair[0]] += 1 
        return AOV, indegreeHash