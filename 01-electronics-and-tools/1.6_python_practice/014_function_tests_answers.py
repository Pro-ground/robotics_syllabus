# Problem 14 — tests that live in their own functions
#
# This file is the worked answer for 014_function_tests.py. Try that file first.

def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def wrap_degrees(deg):
    wrapped = (deg + 180) % 360 - 180
    if wrapped == -180:
        return 180
    return wrapped


def test_clamp_inside():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_low():
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_high():
    assert clamp(12, 0, 10) == 10


def test_wrap_190():
    assert wrap_degrees(190) == -170


def test_wrap_neg_180():
    assert wrap_degrees(-180) == 180


# ----- ASSERTION ------

test_clamp_inside()
test_clamp_below_low()
test_clamp_above_high()
test_wrap_190()
test_wrap_neg_180()

assert clamp(5, 0, 10) == 5
assert clamp(-1, 0, 10) == 0
assert wrap_degrees(190) == -170

print("ok")
