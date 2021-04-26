

# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for neighbor in node.neighbors:
            dfs(neighbor)
            
    return explored

# Breadth-first search
def bfs(start, goal):
    explored = []
    queue = []

    queue.append([start])

    while queue:
        firstPath = queue[0]
        lastNode = firstPath[-1]

        if lastNode not in explored:
            for neighbor in lastNode.neighbors:
                newPath = firstPath.copy()
                newPath.append(neighbor)
                queue.append(newPath)

                if(neighbor is goal):
                    return newPath
                    
            explored.append(lastNode)





    # queue.append('a')
    # queue.pop(0)


