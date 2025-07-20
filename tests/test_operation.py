from src.math_operation import add,sub

def test_add():
    assert add(5,2)==7
    assert add(3,0)==3
    assert add(-1,1)==0
    
def test_sub():
    assert sub(3,2)==1
    assert sub(-1,-1)==0
    assert sub(2,0)==2    