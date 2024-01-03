import math
from typing import List
from collections import UserList

class Vector(UserList):
    def __init__(self,iterable):
        super().__init__(float(item) for item in iterable if type(item) in [float,int])
    
    def magnitude(self):
        _magnitude =0 
        for item in self.data:
            _magnitude+=item*item
        return math.sqrt(_magnitude)

