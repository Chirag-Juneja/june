from collections import UserList
from ..vector import Vector
from typing import * 

class Matrix(UserList):
    def __init__(self,iterable:List):
        if not all(len(v)==len(iterable[0]) for v in iterable):
            raise RuntimeError(f"Column dimensions must match. Got {[len(v) for v in iterable]}")
        super().__init__(Vector(item) for item in iterable if type(item) is list)

    def shape(self)->Tuple[int,int]:
        return len(self.data),len(self.data[0])
    
    def row(self,idx)->Vector:
        return Vector([c[idx] for c in self.data])

    def col(self,idx)->Vector:
        return self.data[idx]

    @classmethod
    def identity(cls, n:int):
        return cls([[1 if col==row else 0 for col in range(n)] for row in range(n)])
