# Problem 14 — tests that live in their own functions
#
# pytest is a tool that finds functions whose names start with test_ and
# runs them. Each test calls a function you own and checks the result
# with assert. If a clamp or a wrap is wrong, a test should say so before
# a robot does.
#
# This file still runs with python, so you do not need pytest installed
# to finish it. If you have pytest, you can also run:
#   pytest 014_function_tests.py
#
# The functions under test are already written. You write the tests.
#
# What you will need
#
# Packages: none required. pytest is optional.
#
# Ideas to have in place before you start:
# - assert left == right stops the program if the two sides differ.
# - A good test names the case: test_clamp_below_low, not test1.
# - Tests should not change each other's data. Make a new list inside
#   the test if you need one (from 006).
#
# Tools to look up if you do not know them yet:
# - assert
# - pytest, if you want the extra runner
#
# Snippets
#
#   def test_clamp_below_low():
#       assert clamp(-1, 0, 10) == 0
#
# ----- Given (do not edit) -----

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


# ----- EXERCISE -----
#
# 1. test_clamp_inside()
#    Assert that clamp(5, 0, 10) is 5.
#    Your answer:

def test_clamp_inside():
    assert False


# 2. test_clamp_below_low()
#    Assert that clamp(-1, 0, 10) is 0.
#    Your answer:

def test_clamp_below_low():
    assert False


# 3. test_clamp_above_high()
#    Assert that clamp(12, 0, 10) is 10.
#    Your answer:

def test_clamp_above_high():
    assert False


# 4. test_wrap_190()
#    Assert that wrap_degrees(190) is -170.
#    Your answer:

def test_wrap_190():
    assert False


# 5. test_wrap_neg_180()
#    Assert that wrap_degrees(-180) is 180.
#    Your answer:

def test_wrap_neg_180():
    assert False


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
