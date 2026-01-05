import math

def use_sqrt(x: float) -> float:
    return math.sqrt(x)

def test_spy(mocker):
    spy = mocker.spy(math, "sqrt")
    assert use_sqrt(9) == 3
    assert spy.call_count == 1
    assert spy.spy_return == 3