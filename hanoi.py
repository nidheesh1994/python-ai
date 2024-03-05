def hanoi(n, start, goal, ignore):
    if n == 1:
        print(start, "->", goal)
        return
    
    hanoi(n-1,start,ignore,goal)
    print(start,"->",goal)
    hanoi(n-1,ignore, goal, start)

hanoi(4,"A","B","C")


#four pin not completed
def hanoi4(n, start, goal, ingore1, ignore2):
    if n == 1:
        print(start,"->",goal)
        return
    
