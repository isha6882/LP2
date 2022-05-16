graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited = set()     # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Depth-First Search:")
dfs(visited, graph, '1')

"""
Graph:
        1
       / \
      2   3
     / \   \
    4   5 - 6

OUTPUT:
Depth-First Search:
1 2 4 5 6 3 

"""