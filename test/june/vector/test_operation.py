from june import vector

def test_add():
    v = [1.0,2.0,3.0]
    w = [1,2,3] 
    result = vector.add(v,w)
    assert result == [2.0, 4.0, 6.0]