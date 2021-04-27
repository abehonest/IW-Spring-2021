

# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for neighbor in node.neighbors:
            dfs(neighbor, explored) # Just realized my main bug - was typing dfs(neighbor) and not (neighbor, explored).  Forgot Python didn't error on that.
    return explored

# Breadth-first search
def bfs(start, goal):
    explored = []
    queue = []

    queue.append([start])
    while len(queue) > 0:

        firstPath = queue.pop(0)
        lastNode = firstPath[-1]



        if lastNode not in explored:
            for neighbor in lastNode.neighbors:
                newPath = list(firstPath)
                newPath.append(neighbor)
                queue.append(newPath)

                if(neighbor is goal):
                    return newPath

            explored.append(lastNode)



# First try with BFS - infinite looping error
# Figured that out.  I forgot to use queue.pop when referencing the first item.  Now getting returned path type is incorrect
# Ahh, my issue was that I did queue.pop[0] instead of queue.pop(0).  My python is rustier than I thought.




