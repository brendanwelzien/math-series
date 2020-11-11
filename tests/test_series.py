from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_three():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


    




