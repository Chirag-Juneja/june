from june import vector
from june.vector import Vector
from collections import Counter
import math

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

def drange(v:Vector)->float:
    return max(v)-min(v)

def variance(v:Vector)->float:
    n = len(v)
    if n<2:
        raise RuntimeError("Vector should have at least 2 elements.")
    xs = mean(v)
    deviations = [x-xs for x in v]
    return Vector(deviations).magnitude()**2/(n-1)

def standard_deviation(v:Vector)->float:
    return math.sqrt(variance(v))

def interquartile_range(v:Vector)->float:
    return quantile(v,0.75)-quantile(v,0.25)

def covariance(v:Vector,w:Vector)->float:
    if len(v)!=len(w):
        raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
    if len(v)<2:
        raise RuntimeError("Vector should have at least 2 elements.")
    v_mean = mean(v)
    w_mean = mean(w)
    v_deviations,w_deviations = [x-v_mean for x in v],[x-w_mean for x in w]
    return vector.dot(v_deviations,w_deviations)/(len(v)-1)

def correlation(v:Vector,w:Vector)->float:
    v_std = standard_deviation(v)
    w_std = standard_deviation(w)
    if w_std > 0 and v_std > 0:
        return covariance(v,w)/v_std/w_std
    return 0
