# The Dijkstra algorithm is similar to Prim's algorthim except that this time
# Dijkstra searches for the minimum path length, and that is the edge accumulation
# While Prim looks for the minimum overall edge accumulation
# ******* Pseudocode***********
# From each of the unvisited vertices, we choose the vertex with the smallest distance and visit it.
# We update the distance for each neighboring vertex, of the visited vertex,
# whose current distance is greater than its sum and the weight of the edge between them.
# This is repeated until all the vertices are visited.


def shortestReach(n, edges, s, ):
    # detect if first time through, set current distance to zero
    visited = []
    distances = {}
    pre_node = {}
    maximum = 10000000

    if not visited: distances[s] = 0
    # if we've found our end node, find the path to it, and return

    if s == n:
        path = []
        while n is not None:
            path.append(n)
            n = pre_node.get(n, None)
        return distances[s], path[::-1]

    # process neighbors as per algorithm, keep track of pre_node
    for adjacent_node in edges[s]:
        if adjacent_node not in visited:
            adjacebt_distance = distances.get(adjacent_node, maximum)
            length = distances[s] + edges[s][adjacent_node]
            if length < adjacebt_distance:
                distances[adjacent_node] = length
                pre_node[adjacent_node] = s
    # neighbors processed, now mark the current node as visited
    visited.append(s)
    # finds the closest unvisited node to the start
    unvisited = dict((k, distances.get(k, maximum)) for k in edges if k not in visited)

    closestnode = min(unvisited, key=unvisited.get)
    # now take the closest node and recurse, making it current
    return shortestReach(edges, closestnode, n)



# Testing
# print(shortestReach(4, [[0, 1, 24], [0, 2, 3], [0, 3, 20], [2, 3, 12]], 0))


# Weakness of code
#  Despite the thorough understanding of this algorithm
# with the step by step explanation to each process, there was a bug
# Nonetheless , the above is the start to this algorithm
