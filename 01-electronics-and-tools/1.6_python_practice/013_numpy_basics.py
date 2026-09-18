# Problem 13 — NumPy basics
# Write a single file, e.g. 013_numpy_basics.py. Requires NumPy.
#
# Install NumPy in the virtual environment from 010 before you start.
#
# What you will need
#
# Packages: NumPy only (import numpy as np). Install it with pip in a
# virtual environment if it is not already there.
#
# Ideas to have in place before you start:
# - The mean of a list, from 1.5_maths_practice/006_mean_and_blend.md
# - A NumPy array is a grid of numbers. A 1D array is a single row of
#   values. A 2D array is rows and columns.
# - Population variance is the average of the squared differences from
#   the mean (divide by n, not n minus 1).
# - A moving average replaces each value with the average of its
#   neighbours. Near the ends, the window is smaller because there are
#   fewer neighbours.
# - Slicing (values[a:b]) takes a stretch of an array without a loop.
#
# Tools to look up if you do not know them yet:
# - np.array, np.mean, np.stack or np.vstack
# - array slicing and arithmetic (array - number, array ** 2)
# - np.where or walking a 2D array with two loops, for the threshold task
# - converting an array back to a Python list if a function must return a list
#
# You do not need: pandas. Do not use numpy.var for sensor_variance; the
# spec asks you to build that from mean, subtract, square, and average.
#
# This is your first exposure to NumPy, the array library that almost every
# robotics tool depends on. If you do not have it installed, run:
#   pip install numpy
# in your virtual environment.
#
# Spec
#
# Implement the following functions using NumPy arrays (numpy.ndarray).
# No external packages beyond numpy.
#
# 1. sensor_variance(values: list[float]) -> float
#    Given a flat list of sensor readings, return the population variance
#    (average of squared deviations from the mean). Do not use numpy.var() —
#    compute it by creating an array, finding the mean, subtracting, squaring,
#    and averaging.
#
# 2. moving_average(values: list[float], window: int) -> list[float]
#    Given a list of readings and a window size, return a list of the same
#    length where each element is the average of the window of that size
#    centred on the element. For positions where the window would extend
#    past the beginning or end of the list, use only the available values.
#    Use NumPy array operations where you can (e.g. slicing and summing
#    across slices) rather than writing nested loops.
#
# 3. threshold_detect(signals: list[list[float]], threshold: float) -> list[tuple]
#    Given a list of signal arrays (each a flat list[float] of equal length)
#    and a threshold, return a list of (index, value) tuples for every
#    element across all signals that exceeds the threshold. Signal arrays
#    should be stacked into a 2D array first.
#
#
# Examples
#
# sensor_variance([1.0, 2.0, 3.0, 4.0, 5.0]) -> 2.0
#
# moving_average([1, 2, 3, 4, 5], 3) -> [1.5, 2.0, 3.0, 4.0, 4.5]
#   index 0: (1)           -> 1.0  (but wait, window=3 should use indices 0,1 -> avg=1.5)
#   index 1: (1,2,3)       -> 2.0
#   index 2: (1,2,3,4) no, centred on 2: indices 1,2,3? No, let's clarify:
#   "centred" means take the window around each element, clipping to bounds.
#   For window=3 at index 0: use indices 0,1 -> [1,2] -> 1.5
#   For window=3 at index 1: use indices 0,1,2 -> [1,2,3] -> 2.0
#   For window=3 at index 2: use indices 1,2,3 -> [2,3,4] -> 3.0
#   For window=3 at index 3: use indices 2,3,4 -> [3,4,5] -> 4.0
#   For window=3 at index 4: use indices 3,4 -> [4,5] -> 4.5
#
#   So: [1.5, 2.0, 3.0, 4.0, 4.5]
#
# threshold_detect([[1, 5, 3], [2, 4, 6]], 3.0) ->
#   [(1, 5.0), (1, 4.0), (2, 6.0)]
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 013_numpy_basics.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----
# Write your code below.
#

#
#
#
#
#
#
#
#
#
#
#
# ----- ASSERTION ------
#

import numpy as np

# --- sensor_variance ---
var = sensor_variance([1.0, 2.0, 3.0, 4.0, 5.0])
assert abs(var - 2.0) < 1e-9, f"Expected 2.0, got {var}"

var2 = sensor_variance([10.0, 10.0, 10.0])
assert abs(var2 - 0.0) < 1e-9, f"Expected 0.0, got {var2}"

var3 = sensor_variance([1.0])
assert abs(var3 - 0.0) < 1e-9

# --- moving_average ---
ma = moving_average([1, 2, 3, 4, 5], 3)
expected = [1.5, 2.0, 3.0, 4.0, 4.5]
assert len(ma) == 5
assert [round(x, 2) for x in ma] == expected

ma2 = moving_average([10, 20, 30], 2)
# index 0: [10,20] -> 15.0
# index 1: [10,20,30] -> 20.0
# index 2: [20,30] -> 25.0
assert [round(x, 2) for x in ma2] == [15.0, 20.0, 25.0]

ma3 = moving_average([1], 5)
assert ma3 == [1.0]

# --- threshold_detect ---
td = threshold_detect([[1, 5, 3], [2, 4, 6]], 3.0)
# Check that all values > 3 are found
assert (1, 5.0) in td
assert (1, 4.0) in td
assert (2, 6.0) in td
assert (0, 1.0) not in td
assert (0, 2.0) not in td
assert (0, 3.0) not in td  # threshold is strictly greater
assert len(td) == 3

td2 = threshold_detect([[1, 2, 3]], 10.0)
assert td2 == []

td3 = threshold_detect([np.array([0, 10, 20]), np.array([5, 15, 25])], 10.0)
values = [v for _, v in td3]
assert 10.0 in values
assert 15.0 in values
assert 20.0 in values
assert 25.0 in values

print("ok")
