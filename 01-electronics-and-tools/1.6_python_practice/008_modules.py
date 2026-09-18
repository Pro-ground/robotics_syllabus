# Problem 8 — import a file and run only as the main program
#
# An import brings names from another file into this one. A package is a
# folder of those files that you can import as a group. The usual guard
#   if __name__ == "__main__":
# means "only run this when I am the file you launched," not when another
# file imported me.
#
# This folder already has a helper file named angle_units.py. Import from
# it. Do not copy its arithmetic into this file.
#
# What you will need
#
# Packages: none extra. You import angle_units from this same folder.
#
# Ideas to have in place before you start:
# - import angle_units gives you angle_units.to_radians.
# - from angle_units import to_radians gives you to_radians directly.
#   Either style is fine.
# - __name__ is a string Python sets. It is "__main__" when this file is
#   the one you ran. It is "008_modules" (or similar) when imported.
# - A default argument is a value used when the caller leaves that input
#   out: def scale(value, gain=1.0).
#
# Tools to look up if you do not know them yet:
# - import, from ... import ...
# - if __name__ == "__main__":
#
# You do not need: pip, NumPy, or a package folder yet. 007 is the lab
# for a virtual environment.
#
# Snippets
#
#   import angle_units
#   rad = angle_units.to_radians(180)
#
#   def run_if_main(module_name, fn):
#       if module_name == "__main__":
#           return fn()
#       return None
#
#   def scale(value, gain=1.0):
#       return value * gain
#
# ----- EXERCISE -----
#
# 1. heading_radians(deg)
#    Convert deg to radians by calling the helper in angle_units.py.
#    Do not multiply by a constant yourself.
#    Your answer:

def heading_radians(deg):
    pass


# 2. scale_reading(value, gain=1.0)
#    Return value multiplied by gain. If the caller omits gain, use 1.0.
#    Your answer:

def scale_reading(value, gain=1.0):
    pass


# 3. run_if_main(module_name, fn)
#    If module_name is the string "__main__", call fn() with no arguments
#    and return whatever fn returned.
#    Otherwise return None and do not call fn.
#    This is the same decision as if __name__ == "__main__":, with the
#    name passed in so the tests can fake it.
#    Your answer:

def run_if_main(module_name, fn):
    pass


# ----- ASSERTION ------

import math

import angle_units

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
