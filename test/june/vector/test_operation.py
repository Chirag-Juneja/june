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

