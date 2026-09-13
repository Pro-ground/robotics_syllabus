# Problem 8 — reading sensor data with a class
# Write a single file, e.g. 008_reading_class.py. No external packages, only the stdlib.
#
# Do the files in this folder in numbered order. This is 008 of 013.
#
# What you will need
#
# Packages: none. Use only what Python gives you with no install.
#
# Ideas to have in place before you start:
# - A class is a blueprint for a kind of object. You write the blueprint
#   once, then make as many objects as you need.
# - Methods are functions that belong to the class. Their first argument is
#   always self: the particular object the method was called on.
# - __init__ runs when you create an object. It stores the starting data.
# - None is the value that means "no result" when a mean or min has no
#   matching readings.
#
# Tools to look up if you do not know them yet:
# - class, def, self, __init__
# - storing values as attributes (self.name, self.value)
# - list.append
# - a for loop to walk the stored readings (from 003)
# - / for a mean, and comparing with == (from 001 and 002)
#
# You do not need: files, NumPy, or extra packages. Do not import anything.
#
# 1. SensorReading (class)
#    Represents a single sensor reading.
#    - __init__(self, name: str, value: float, unit: str)
#      Store name, value, and unit as instance attributes.
#    - formatted(self) -> str
#      Return a string in this exact shape: "<name>: <value> <unit>"
#      Example: "temp: 21.5 C"
#    - is_above(self, threshold: float) -> bool
#      Return True if value > threshold, False otherwise.
#
# 2. SensorLog (class)
#    Holds a collection of SensorReading objects and provides summary methods.
#    - __init__(self)
#      Start with an empty list of readings.
#    - add(self, reading: SensorReading) -> None
#      Append the reading to the list. Do not check for duplicates.
#    - readings_for(self, name: str) -> list[SensorReading]
#      Return a new list of SensorReading objects whose name matches, in the order added.
#      Return an empty list if no readings match.
#    - mean_of(self, name: str) -> float | None
#      Return the arithmetic mean of all values for the given name.
#      Return None if no readings match that name.
#    - min_of(self, name: str) -> float | None
#      Return the minimum value for the given name, or None if no readings match.
#    - max_of(self, name: str) -> float | None
#      Return the maximum value for the given name, or None if no readings match.
#    - count(self, name: str) -> int
#      Return how many readings exist for the given name. Return 0 if none.
#
#
# Examples
#
# # SensorReading
# r = SensorReading("temp", 21.5, "C")
# r.formatted()       ->  "temp: 21.5 C"
# r.is_above(20.0)    ->  True
# r.is_above(22.0)    ->  False
#
# # SensorLog
# log = SensorLog()
# log.add(SensorReading("temp", 21.5, "C"))
# log.add(SensorReading("dist", 0.4, "m"))
# log.add(SensorReading("temp", 22.0, "C"))
# log.add(SensorReading("dist", 0.3, "m"))
# log.count("temp")           ->  2
# log.count("pressure")       ->  0
# log.mean_of("temp")         ->  21.75
# log.min_of("dist")          ->  0.3
# log.max_of("dist")          ->  0.4
# log.mean_of("pressure")     ->  None
# len(log.readings_for("temp")) ->  2
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 008_reading_class.py
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

assert SensorReading("temp", 21.5, "C").formatted() == "temp: 21.5 C"
assert SensorReading("dist", 0.4, "m").formatted() == "dist: 0.4 m"
assert SensorReading("battery", 12, "V").formatted() == "battery: 12 V"
assert SensorReading("temp", 21.5, "C").is_above(20.0) is True
assert SensorReading("temp", 21.5, "C").is_above(22.0) is False
assert SensorReading("temp", 5.0, "C").is_above(5.0) is False

assert SensorReading("temp", 21.5, "C").is_above(100.0) is False

log = SensorLog()
log.add(SensorReading("temp", 21.5, "C"))
log.add(SensorReading("dist", 0.4, "m"))
log.add(SensorReading("temp", 22.0, "C"))
log.add(SensorReading("dist", 0.3, "m"))

assert log.count("temp") == 2
assert log.count("dist") == 2
assert log.count("pressure") == 0

assert log.mean_of("temp") == 21.75
assert log.min_of("dist") == 0.3
assert log.max_of("dist") == 0.4
assert log.mean_of("pressure") is None
assert log.min_of("pressure") is None
assert log.max_of("pressure") is None

temps = log.readings_for("temp")
assert len(temps) == 2
assert temps[0].value == 21.5
assert temps[1].value == 22.0

empty = log.readings_for("pressure")
assert empty == []

# Edge: single reading
log2 = SensorLog()
log2.add(SensorReading("x", 10.0, "unit"))
assert log2.mean_of("x") == 10.0
assert log2.min_of("x") == 10.0
assert log2.max_of("x") == 10.0

print("ok")
