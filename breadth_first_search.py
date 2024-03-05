def breadth_first_search(problem, candidates, visited = set()):

    if not candidates: return

    c = candidates.pop(0)
    node = c[-1]

    # token = problem.token(node)

    # if token in visited: return

    # visited = visited.union(set([token]))

    if problem.goal(node) : return c

    succ = [s for s in problem.succ(node)]

    for s in succ:
        candidates.append(c + [s])

    return breadth_first_search(problem, candidates, visited)