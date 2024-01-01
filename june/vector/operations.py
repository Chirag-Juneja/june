from .types import * 
import builtins


def add(v:Vector,w:Vector)->Vector:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   return [vi+wi for vi,wi in zip(v,w)]

def subtract(v:Vector,w:Vector)->Vector:
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimensions must match. Got {len(v)} and {len(w)}.")
   return [vi-wi for vi,wi in zip(v,w)]

def sum(vectors:List[Vector])->Vector:
   if not all([len(v)==len(vectors[0]) for v in vectors]):
      raise RuntimeError(f"Vector dimensions must match. Got {[len(v) for v in vectors]}.")
   return [builtins.sum(v[i] for v in vectors) for i in range(len(vectors[0]))]

def mul(vector:Vector,scalar:float)->Vector:
   return [scalar*vi for vi in vector]
