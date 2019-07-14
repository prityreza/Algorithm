graph1 = {
    1 : [2,3],
    2 : [4,5],
    4 : [6],
    6 :[],
    3 :[],
    5 :[]
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


print(dfs(graph1,1, []))