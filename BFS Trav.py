import collections
def bfs(graph, root):
    visited, queue= [], [root]
    while queue:
        vertex = queue.pop(0)
        prnt(vertex)
        for node in graph[vertex]:
            if node not in visited:
                visited.append(node)
                queue.append(node)

def prnt(vertex):
    print(vertex,end=' ')

graph = {0: [1, 2], 1: [2,3], 2: [3], 3: [1,2]}
bfs(graph, 0)