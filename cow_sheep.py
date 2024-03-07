import time

def successors(stable):

    empty = stable.index("_")

    candidates = [empty-2, empty-1, empty+1, empty+2]
    
    candidates = [ c for c in candidates if c >= 0 and c < len(stable) and (
                  stable[c:c+2] == ["C","_"] or
                  stable[c-1:c+1] == ["_","S"] or
                  stable[c:c+3] == ["C","S","_"] or
                  stable[c-2:c+1] == ["_","C","S"] )
                  ]
    assert not [c for c in candidates if stable[c] == "_"]
    
    for c in candidates:
        new_stable = stable[:]

        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
        yield new_stable

goal_stable = ["S","S","S","S","_","C","C","C","C"]
stable = ["C","C","C","C","_","S","S","S","S"]

def solution(stable):
    if stable == goal_stable:
        return [stable]
    
    for new_stable in successors(stable):
        sol = solution(new_stable)
        if(sol):
            return [stable] + sol

for sol in solution(stable):
    print(sol)
    time.sleep(1)