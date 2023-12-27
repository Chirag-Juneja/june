from .types import * 

def add(v:Vector,w:Vector):
   if len(v)!=len(w):
      raise RuntimeError(f"Vector dimentions must match. Got {len(v)} and {len(w)}")
   return [vi+wi for vi,wi in zip(v,w)]