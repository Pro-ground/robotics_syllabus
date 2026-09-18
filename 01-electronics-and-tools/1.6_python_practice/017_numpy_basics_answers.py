# Problem 17 — NumPy arrays
#
# This file is the worked answer for 017_numpy_basics.py. Try that file first.

import numpy as np


def sensor_variance(values):
    arr = np.array(values, dtype=float)
    mean = np.mean(arr)
    return float(np.mean((arr - mean) ** 2))


def moving_average(values, window):
    arr = np.array(values, dtype=float)
    n = len(arr)
    half = window // 2
    out = []
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        out.append(float(np.mean(arr[lo:hi])))
    return out


def threshold_detect(signals, threshold):
    stacked = np.vstack([np.array(signal, dtype=float) for signal in signals])
    found = []
    rows, cols = stacked.shape
    for r in range(rows):
        for c in range(cols):
            value = float(stacked[r, c])
            if value > threshold:
                found.append((c, value))
    return found


# ----- ASSERTION ------

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
