from june.vector import Vector
from collections import Counter

def mean(v:Vector)->float:
    return sum(v)/len(v)

def median(v:Vector)->float:
    n = len(v)
    if not n :
        raise RuntimeError("Cannot find median of empty vector")
    if n%2!=0:
        return v[n//2]
    else:
        return (v[n//2]+v[n//2-1])/2
    
def quantile(v:Vector,p:float)->float:
    p_index = int(p*len(v))
    return sorted(v)[p_index]

def mode(v:Vector)->float:
    counter = Counter(v)
    max_count = max(counter.values())
    for x,count in counter.items():
        if count == max_count:
            return x 

