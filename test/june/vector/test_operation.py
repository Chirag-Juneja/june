import pytest
from june import vector

def test_add():
    v = [1.0,2.0,3.0]
    w = [1,2,3] 
    result = vector.add(v,w)
    assert result == [2.0, 4.0, 6.0]

def test_add_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    with pytest.raises(RuntimeError):
        result = vector.add(v,w)

def test_subtract():
    v = [1.0,2.0,3.0]
    w = [1,2,3] 
    result = vector.subtract(v,w)
    assert result == [0.0, 0.0, 0.0]

def test_subtract_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    with pytest.raises(RuntimeError):
        result = vector.subtract(v,w)

def test_sum():
    v = [1.0,2.0,3.0]
    w = [1,2,3]
    x=[1,2,3] 
    result = vector.sum([v,w,x])
    assert result == [3.0, 6.0, 9.0]

def test_sum_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    x=[1,2,3] 
    with pytest.raises(RuntimeError):
        result = vector.sum([v,w,x])

def test_mul():
    v = [1,2,3]
    result = vector.mul(v,5)
    assert result == [5.,10.,15.]

def test_mean():
    v = [1.0,2.0,3.0]
    w = [1,2,3]
    x=[1,2,3] 
    result = vector.mean([v,w,x])
    assert result == [1.0, 2.0, 3.0]

def test_mean_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    x=[1,2,3] 
    with pytest.raises(RuntimeError):
        result = vector.mean([v,w,x])

def test_dot():
    v = [1.0,2.0,3.0]
    w =[4,5,6]
    result = vector.dot(v,w)
    assert result == 32

def test_dot_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    with pytest.raises(RuntimeError):
        result = vector.dot(v,w)

def test_magnitude():
    v=[3,4]
    result = vector.magnitude(v)
    assert result == 5

def test_distance():
    v=[4,5]
    w=[1,1]
    result = vector.distance(v,w)
    assert result == 5

def test_distance_invalid_size():
    v = [1.0,2.0,3.0]
    w = [1,2,3,4] 
    with pytest.raises(RuntimeError):
        result = vector.dot(v,w)
