import builtins
import math
from .types import * 


def add(v:Vector,w:Vector)->Vector:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   return Vector([vi+wi for vi,wi in zip(v,w)])

def subtract(v:Vector,w:Vector)->Vector:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   return Vector([vi-wi for vi,wi in zip(v,w)])

def sum(vectors:List[Vector])->Vector:
   if not all([len(v)==len(vectors[0]) for v in vectors]):
      raise RuntimeError(f"Vector dimensions must match. Got {[len(v) for v in vectors]}.")
   return Vector([builtins.sum(v[i] for v in vectors) for i in range(len(vectors[0]))])

def mul(vector:Vector,scalar:float)->Vector:
   return Vector([scalar*vi for vi in vector])

def mean(vectors:List[Vector])->Vector:
   if not all([len(v)==len(vectors[0]) for v in vectors]):
      raise RuntimeError(f"Vector dimensions must match. Got {[len(v) for v in vectors]}.")
   n = len(vectors)
   return mul(sum(vectors),1/n)

def dot(v:Vector,w:Vector)->float:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   return builtins.sum(vi*wi for vi,wi in zip(v,w))

def distance(v:Vector,w:Vector)->float:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   sub = subtract(v,w)
   return sub.magnitude()