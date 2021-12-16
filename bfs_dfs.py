def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited

def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, next, goal, path + [next])

def shortest_path_recursive(graph, start, goal):
    try:
        return next(dfs_paths_recursive(graph, start, goal))
    except StopIteration:
        return None

if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    print(bfs(graph, 'A'))
    print(bfs_paths(graph, 'A', 'F'))
    print(shortest_path(graph, 'A', 'F'))
    print(dfs(graph, 'A'))
    print(dfs_paths(graph, 'A', 'F'))
    print(shortest_path(graph, 'A', 'F'))
    print(dfs_recursive(graph, 'A'))
    print(list(dfs_paths_recursive(graph, 'A', 'F')))
    print(shortest_path_recursive(graph, 'A', 'F'))
