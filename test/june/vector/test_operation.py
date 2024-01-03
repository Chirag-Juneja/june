import pytest
from june import vector

def test_add():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3]) 
    result = vector.add(v,w)
    assert result == vector.Vector([2.0, 4.0, 6.0])

def test_add_invalid_size():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3,4]) 
    with pytest.raises(RuntimeError):
        result = vector.add(v,w)

def test_subtract():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3]) 
    result = vector.subtract(v,w)
    assert result == vector.Vector([0.0, 0.0, 0.0])

def test_subtract_invalid_size():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3,4])
    with pytest.raises(RuntimeError):
        result = vector.subtract(v,w)

def test_sum():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3])
    x = vector.Vector([1,2,3]) 
    result = vector.sum([v,w,x])
    assert result == vector.Vector([3.0, 6.0, 9.0])

def test_sum_invalid_size():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3,4])
    x = vector.Vector([1,2,3]) 
    with pytest.raises(RuntimeError):
        result = vector.sum([v,w,x])

def test_mul():
    v = vector.Vector([1,2,3])
    result = vector.mul(v,5)
    assert result == vector.Vector([5.,10.,15.])

def test_mean():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3])
    x = vector.Vector([1,2,3]) 
    result = vector.mean([v,w,x])
    assert result == vector.Vector([1.0, 2.0, 3.0])

def test_mean_invalid_size():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3,4])
    x = vector.Vector([1,2,3]) 
    with pytest.raises(RuntimeError):
        result = vector.mean([v,w,x])

def test_dot():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([4,5,6])
    result = vector.dot(v,w)
    assert result == 32

def test_dot_invalid_size():
    v = vector.Vector([1.0,2.0,3.0])
    w = vector.Vector([1,2,3,4])
    with pytest.raises(RuntimeError):
        result = vector.dot(v,w)

def test_magnitude():
    v=vector.Vector([3,4])
    result = v.magnitude()
    assert result == 5

def test_distance():
    v=vector.Vector([4,5])
    w=vector.Vector([1,1])
    result = vector.distance(v,w)
    assert result == 5

def test_distance_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    with pytest.raises(RuntimeError):
        result = vector.dot(v,w)
