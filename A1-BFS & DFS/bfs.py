graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited = []    # List for visited nodes.
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print(m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Breadth-First Search: ")
bfs(visited, graph, '1')

"""
Graph:
        1
       / \
      2   3
     / \   \
    4   5 - 6

OUTPUT:
Breadth-First Search: 
1 2 3 4 5 6 

"""