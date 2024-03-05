class Doll:
    def __init__(self, child, index):
        self.child = child
        self.index = index
    
    def open(self):
        return self.child



def count_nested_dolls(doll):

    child = doll.open()

    if not child: return 1
    
    return 1 + count_nested_dolls(child)



d1 = Doll(None,1)
d2 = Doll(d1,2)
d3 = Doll(d2,3)
d4 = Doll(d3,4)
print("Count", count_nested_dolls(d4))