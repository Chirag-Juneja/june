import pytest
from june import matrix


def test_Matrix_dimension():
    m = [[2,3,4],[1,3]]
    with pytest.raises(RuntimeError):
        m = matrix.Matrix(m)


def test_Matrix_shape():
    m = [[2,3,4],[1,3,4]]
    m = matrix.Matrix(m).shape()
    assert m == (2,3) 