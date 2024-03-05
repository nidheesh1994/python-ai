def depth_first_search(problem, node, visited = set()):

    token = problem.token(node)

   
    if token in visited: return

    
    visited = visited.union(set([token]))

    if problem.goal(node): return [node]

    for n_succ in problem.succ(node):
        sol = depth_first_search(problem, n_succ, visited)

        if sol:
            return [node] + sol