import program11 as p11
def test_maximum_first():
    v1 = 1
    v2 = 2
    ret = p11.maximum(v1,v2)
    assert ret == 2

def test_maximum_second():
    v1 = 2
    v2 = 1
    ret = p11.maximum(v1,v2)
    assert ret == 2

def test_maximum_bothEqual():
    v1 = 1
    v2 = 1
    assert v1 == v2