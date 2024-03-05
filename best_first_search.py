import heapq
import path

def best_first_search(problem, candidates):
    if not candidates: return


    cand = heapq.heappop(candidates)

    node = cand.current()

    if problem.goal(node): return cand

    for succ_node in problem.succ(node):
        heapq.heappush(candidates, cand.append(succ_node))
    
    return best_first_search(problem, candidates)
