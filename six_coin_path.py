from path import *

class SixCoinPath(Path):

    def __repr__(self):
        
        return "\n".join(" ".join(str(n) for n in node ) for node in self.path)