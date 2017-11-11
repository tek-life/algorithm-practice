class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        result = []
        queue = []
        edge = {i:[] for i in range(numCourses)}
        degrees =[0 for _ in range(numCourses)]
        for x in prerequisites:
            if x[0] not in edge[x[1]]:
                degrees[x[0]] += 1
                edge[x[1]].append(x[0])
            
        for i,x in enumerate(degrees):
            if x == 0:
                queue.append(i)
                
        while len(queue) != 0:
            n = queue[0]
            for node in edge[n]:
                degrees[node] -= 1
                if degrees[node] == 0:
                    queue.append(node)
                    
            result.append(n)
            queue.remove(n)
        
        if len(result) != numCourses:
            return []
        return result
