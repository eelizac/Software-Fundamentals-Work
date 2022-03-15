from neighbours import neighbours
# testing 

def test_valid(): 
    assert list(neighbours([1,2,3,4])) == [(1,2), (1,2,3), (2,3,4), (3,4)]
