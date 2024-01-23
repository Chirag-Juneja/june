import pytest
import math
import statistics
from june.vector import Vector
from june import stats


def test_mean():
    v = Vector([1,2,3,4,5])
    assert stats.mean(v) == 3.0

def test_median_odd_len():
    v = Vector([1,2,3,4,5])
    assert stats.median(v)==3.0

def test_median_even_len():
    v = Vector([1,2,3,4,5,6])
    assert stats.median(v)==3.5

def test_median_empty():
    v = Vector([])
    with pytest.raises(RuntimeError):
        stats.median(v)

def test_quantile():
    v = Vector([1,1,2,2,3,4,5,6,7,8])
    assert stats.quantile(v,0.2)==2.0
    assert stats.quantile(v,0.8)==7.0
    assert stats.quantile(v,0.9)==8.0

def test_mode():
    v = Vector([1,1,2,2,3,4,5,6,7,8])
    assert stats.mode(v)==1.0
    assert stats.mode(v[1:])==2.0

def test_range():
    v = Vector([3,4,5])
    result =stats.drange(v)
    assert result == 2.0

def test_variance():
    l = [1,1,2,2,3,4,5,6,7,8]
    v = Vector(l)
    result = stats.variance(v)
    assert round(result,5) == round(statistics.variance(l),5)

def test_standard_deviation():
    l = [1,1,2,2,3,4,5,6,7,8]
    v = Vector(l)
    result = stats.standard_deviation(v)
    assert round(result,5) == round(math.sqrt(statistics.variance(l)),5)

def test_interquartile_range():
    l = [1,2,3,4,5,6,7,8,9,10]
    v= Vector(l)
    result = stats.interquartile_range(v)
    assert result == 5

def test_covariance():
    l = [1,1,2,2,3,4,5,6,7,8]
    m = [-1,-1,2,3,4,-4,-5,6,7,8]
    result = stats.covariance(Vector(l),Vector(m))
    assert round(statistics.covariance(l,m),5) == round(result,5)

def test_covariance_unequal():
    l = [1,1,2,2,3,4,5,6,7,8]
    m = [1,2,3,4,-4,-5,6,7,8]
    with pytest.raises(RuntimeError):
        stats.covariance(Vector(l),Vector(m))
    
def test_correlation():
    l = [1,1,2,2,3,4,5,6,7,8]
    m = [-1,-1,2,3,4,-4,-5,6,7,8]
    result = stats.correlation(Vector(l),Vector(m))
    assert round(statistics.correlation(l,m),5) == round(result,5)

def test_correlation_unequal():
    l = [1,1,2,2,3,4,5,6,7,8]
    m = [1,2,3,4,-4,-5,6,7,8]
    with pytest.raises(RuntimeError):
        stats.correlation(Vector(l),Vector(m))
    
