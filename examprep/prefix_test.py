from prefix import prefix_search 
import pytest 

def test_valid(): 
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") ==  {'ac': 1, 'ab': 3}

def test_empty_dict(): 
    assert prefix_search({}, "a") ==  {}


def test_none(): 
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "zoe") ==  {}

def test_none(): 
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "zoe") ==  {}