def insertion(e,s):
    for i in range(len(s)+1):
        print("insertion: ",s[:i] + [e] + s[i:])
        yield s[:i] + [e] + s[i:]



# for t in insertion(2, [3]):
#     print(t)

def perm(s):
    if s == []:
        yield []
    else:
        e, s1 = s[0], s[1:]
        print("e", e, "s1",s1)
        for s1p in perm(s1):
            print("s1p",s1p)
            for p in insertion(e, s1p):
                yield p

for i in perm([1,2,3]):
    print("Final",i)

