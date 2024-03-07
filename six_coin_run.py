import six_coin
from depth_first_search import *
from breadth_first_search import *
from best_first_search import *
import six_coin_path
import sys
sys.setrecursionlimit(100000)

s = six_coin.SixCoin()

paths = depth_first_search(s,s.start())

# print("Depth first search")
# for p in paths:
#     print(p)

# print("\n\n Breadth first search")
# paths = breadth_first_search(s, [[s.start()]])
# for p in paths:
    # print(p)

print("\n\nBest first search")
start_path = six_coin_path.SixCoinPath(path = [s.start()], length=1)
paths = best_first_search(s, [start_path])
print(paths)


