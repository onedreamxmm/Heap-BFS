'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Time Complexity: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.

Space Complexity: O(N), the space used to store the color.
'''


from collections import deque
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        colored = {}
        for node in range(n):
            if node not in colored:
                colored[node] = 1
                queue = deque([node])
                while queue:
                    cur = queue.popleft()
                    for nei in graph[cur]:
                        if nei not in colored:
                            colored[nei] = 1 - colored[cur]
                            queue.append(nei)
                        elif colored[nei] == colored[cur]:
                            return False
        return True

if __name__ == '__main__':
    graph = [[1,3],[0,2],[1,3],[0,2]]
    o = Solution()
    print(o.isBipartite(graph))