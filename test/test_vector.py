from src.vector import Vector

def test_make_vector():
    v=Vector([1,2,3])
    assert len(v.nums) ==3

def test_dimensions():
    v = Vector([5,6,7,4])
    assert v.dims == 4

def test_norm():
    v = Vector([3,4])
    assert v.norm ==5