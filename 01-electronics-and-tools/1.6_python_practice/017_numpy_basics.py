# Problem 17 — NumPy arrays
#
# A NumPy array is a grid of numbers. A 1D array is a single row of
# values. A 2D array is rows and columns. Robotics code uses arrays for
# poses and scans so you can operate on many samples without a Python
# loop over every one.
#
# Install NumPy in the virtual environment from 007 before you start:
#   python -m pip install numpy
#
# Do 1.5_maths_practice/006_mean_and_blend.md before this file if you
# have not yet.
#
# What you will need
#
# Packages: NumPy only (import numpy as np).
#
# Ideas to have in place before you start:
# - The mean of a list is the sum divided by how many items there are.
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
# - converting an array back to a Python list if a function must return a list
#
# You do not need: pandas. Do not use numpy.var for sensor_variance; the
# spec asks you to build that from mean, subtract, square, and average.
#
# Snippets
#
#   import numpy as np
#   arr = np.array([1.0, 2.0, 3.0])
#   mean = np.mean(arr)
#   centred = arr - mean
#   squared = centred ** 2
#
#   window = arr[0:2]
#   # window is the first two values
#
# ----- EXERCISE -----
#
# 1. sensor_variance(values)
#    values is a flat list of sensor readings.
#    Return the population variance (average of squared deviations from
#    the mean). Do not use numpy.var() — create an array, find the mean,
#    subtract, square, and average.
#
#    Examples
#    sensor_variance([1.0, 2.0, 3.0, 4.0, 5.0]) -> 2.0
#    Your answer:

def sensor_variance(values):
    pass


# 2. moving_average(values, window)
#    values is a list of readings. window is an integer size.
#    Return a list of the same length where each element is the average
#    of the window of that size centred on the element. For positions
#    where the window would extend past the beginning or end of the list,
#    use only the available values.
#    Use NumPy array operations where you can (for example slicing)
#    rather than nested loops over every neighbour pair.
#
#    Examples
#    moving_average([1, 2, 3, 4, 5], 3) -> [1.5, 2.0, 3.0, 4.0, 4.5]
#      index 0, window 3: values at 0, 1 -> 1.5
#      index 1, window 3: values at 0, 1, 2 -> 2.0
#      index 2, window 3: values at 1, 2, 3 -> 3.0
#      index 3, window 3: values at 2, 3, 4 -> 4.0
#      index 4, window 3: values at 3, 4 -> 4.5
#    Your answer:

def moving_average(values, window):
    pass


# 3. threshold_detect(signals, threshold)
#    signals is a list of signal arrays (each a flat list of numbers of
#    equal length). Stack them into a 2D array first.
#    Return a list of (index, value) pairs for every element across all
#    signals that is strictly greater than threshold. index is the
#    position along the signal (0, 1, 2, ...), not which signal it came
#    from.
#
#    Examples
#    threshold_detect([[1, 5, 3], [2, 4, 6]], 3.0) ->
#      pairs that include (1, 5.0), (1, 4.0), and (2, 6.0)
#    Your answer:

def threshold_detect(signals, threshold):
    pass


# ----- ASSERTION ------

import numpy as np

var = sensor_variance([1.0, 2.0, 3.0, 4.0, 5.0])
assert abs(var - 2.0) < 1e-9, f"Expected 2.0, got {var}"

var2 = sensor_variance([10.0, 10.0, 10.0])
assert abs(var2 - 0.0) < 1e-9, f"Expected 0.0, got {var2}"

var3 = sensor_variance([1.0])
assert abs(var3 - 0.0) < 1e-9

ma = moving_average([1, 2, 3, 4, 5], 3)
expected = [1.5, 2.0, 3.0, 4.0, 4.5]
assert len(ma) == 5
assert [round(x, 2) for x in ma] == expected

ma2 = moving_average([10, 20, 30], 2)
assert [round(x, 2) for x in ma2] == [15.0, 20.0, 25.0]

ma3 = moving_average([1], 5)
assert ma3 == [1.0]

td = threshold_detect([[1, 5, 3], [2, 4, 6]], 3.0)
assert (1, 5.0) in td
assert (1, 4.0) in td
assert (2, 6.0) in td
assert (0, 1.0) not in td
assert (0, 2.0) not in td
assert (0, 3.0) not in td
assert len(td) == 3

td2 = threshold_detect([[1, 2, 3]], 10.0)
assert td2 == []

td3 = threshold_detect([np.array([0, 10, 20]), np.array([5, 15, 25])], 10.0)
values = [v for _, v in td3]
assert 10.0 not in values
assert 15.0 in values
assert 20.0 in values
assert 25.0 in values

print("ok")
