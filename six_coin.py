def select_candidates(candidates):

    for first in range(len(candidates)-1):
        if candidates[first] != None and candidates[first+1] != None:
            yield [first, first+1]

def select_empty_positions(candidates):

    length = len(candidates)
    empty_inside = [ [c,c+1] for c in range(length) if candidates[c] == None and candidates[c+1] == None]
    return [[-2,-1]] + empty_inside + [[length, length+1]]

def sanitize(state):
    return [c for c in state if c != None ]

def ltrim(state):
    if state[0] == None:
        return ltrim(state[1:])
    else:
        return state

def rtrim(state):
    if state[len(state)-1] == None:
        return rtrim(state[:-1])
    else:
        return state

def trim(state):
    return ltrim(rtrim(state))

def exchange(e,c, state):
    new_state = state[:]
    c0, c1 = new_state[c[0]], new_state[c[1]]
    new_state[c[0]] = None
    new_state[c[1]] = None
    if e[1] == -1:
        new_state.insert(0,c1)
        new_state.insert(0,c0)
    elif e[0] == len(new_state):
        new_state.append(c0)
        new_state.append(c1)
    else:
        new_state[e[0]] = c0
        new_state[e[1]] = c1
    
    
    return new_state

# for c in select_empty_positions(["A","B",None, None,"A","B",None,"A","B","A","B"]):
#     print(c)
        
class SixCoin:

    goal_state = ["A","A","A","B","B","B"]

    def start(self, state = ["A","B","A","B","A","B"]):
        return state
    
    def token(self, state):
        token = ""
        for s in state:
            token+=str(s)
        return token
    
    def goal(self, state):
        return self.goal_state == trim(state)
    
    def succ(self, state):

        for c in select_candidates(state):
            new_state = state[:]

            empty = select_empty_positions(new_state)
            for e in empty:
                if (e[1] != -1 or c[0] != 0) and (c[1] != len(new_state)-1 or e[0] != len(new_state)):
                    final_state = exchange(e,c,new_state)
                    if trim(final_state) != trim(new_state):
                        yield trim(final_state)

            

# s = SixCoin()

# for state in s.succ(s.start()):
#     print(state)