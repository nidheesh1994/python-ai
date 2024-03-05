def successors(stable):

    empty = stable.index("E")

    candidates = [empty-2, empty-1, empty+1, empty+2]
    
    candidates = [ c for c in candidates if c >= 0 and c < len(stable) and (
                  stable[c:c+2] == ["C","E"] or
                  stable[c-1:c+1] == ["E","S"] or
                  stable[c:c+3] == ["C","S","E"] or
                  stable[c-2:c+1] == ["E","C","S"] )
                  ]
    assert not [c for c in candidates if stable[c] == "E"]
    
    for c in candidates:
        new_stable = stable[:]

        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
        yield new_stable

goal_stable = ["S","S","S","S","E","C","C","C","C"]
stable = ["C","C","C","C","E","S","S","S","S"]

def solution(stable):
    if stable == goal_stable:
        return [stable]
    
    for new_stable in successors(stable):
        sol = solution(new_stable)
        if(sol):
            return [stable] + sol

for sol in solution(stable):
    print(sol)