# Problem 8 — import a file and run only as the main program
#
# This file is the worked answer for 008_modules.py. Try that file first.

import angle_units


def heading_radians(deg):
    return angle_units.to_radians(deg)


def scale_reading(value, gain=1.0):
    return value * gain


def run_if_main(module_name, fn):
    if module_name == "__main__":
        return fn()
    return None


# ----- ASSERTION ------

import math

assert abs(heading_radians(180) - math.pi) < 1e-12
assert abs(heading_radians(0) - 0.0) < 1e-12
assert abs(heading_radians(90) - angle_units.to_radians(90)) < 1e-12

assert scale_reading(10) == 10.0
assert scale_reading(10, 2.0) == 20.0
assert scale_reading(10, gain=0.5) == 5.0

calls = []


def marker():
    calls.append("ran")
    return 7


assert run_if_main("008_modules", marker) is None
assert calls == []
assert run_if_main("__main__", marker) == 7
assert calls == ["ran"]

print("ok")
