import pytest
import math
import statistics
from june import vector
from june import stats


def test_mean():
    v = vector.Vector([1,2,3,4,5])
    assert stats.mean(v) == 3.0

def test_median_odd_len():
    v = vector.Vector([1,2,3,4,5])
    assert stats.median(v)==3.0

def test_median_even_len():
    v = vector.Vector([1,2,3,4,5,6])
    assert stats.median(v)==3.5

def test_median_empty():
    v = vector.Vector([])
    with pytest.raises(RuntimeError):
        stats.median(v)

def test_quantile():
    v = vector.Vector([1,1,2,2,3,4,5,6,7,8])
    assert stats.quantile(v,0.2)==2.0
    assert stats.quantile(v,0.8)==7.0
    assert stats.quantile(v,0.9)==8.0

def test_mode():
    v = vector.Vector([1,1,2,2,3,4,5,6,7,8])
    assert stats.mode(v)==1.0
    assert stats.mode(v[1:])==2.0

def test_range():
    v = vector.Vector([3,4,5])
    result =stats.drange(v)
    assert result == 2.0

def test_variance():
    l = [1,1,2,2,3,4,5,6,7,8]
    v = vector.Vector(l)
    result = stats.variance(v)
    assert round(result,5) == round(statistics.variance(l),5)

def test_standard_deviation():
    l = [1,1,2,2,3,4,5,6,7,8]
    v = vector.Vector(l)
    result = stats.standard_deviation(v)
    assert round(result,5) == round(math.sqrt(statistics.variance(l)),5)

def test_interquartile_range():
    l = [1,2,3,4,5,6,7,8,9,10]
    v= vector.Vector(l)
    result = stats.interquartile_range(v)
    assert result == 5