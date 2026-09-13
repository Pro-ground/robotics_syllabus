# Problem 11 — group sensor logs and compute stats
# Write a single file, e.g. 011_aggregate_sensors.py. No external packages, only the stdlib.
#
# Do the files in this folder in numbered order. This is 011 of 013.
# This file uses the loops from 003; it does not teach them for the first time.
#
# What you will need
#
# Packages: none. Use only what Python gives you with no install.
#
# Ideas to have in place before you start:
# - A tuple is an ordered collection written with commas, often in
#   parentheses. You can unpack it: name, value, unit = row.
# - A dict can map a sensor name to a list of that sensor's readings.
# - The spec asks you to build mean, min, and max by walking the list
#   yourself, so you practise the loop, not the built-in helpers.
#
# Tools to look up if you do not know them yet:
# - open and a for loop over a file (from 006 and 003)
# - str.split and str.strip
# - float(...) to turn text into a number
# - dict key lookup and "if key not in the dict, start a list"
# - list.append
#
# You do not need: csv, json, NumPy, or sum / min / max on the values
# (the spec forbids those on the value list). You may use len() on a list.
#
# 1. parse_sensor_log(filename: str) -> list[tuple]
#    Reads a plain-text file where each non-empty line has the format:
#      sensor_name value unit
#    (space-separated, no header row).
#    Returns a list of (sensor_name, float_value, unit) tuples.
#    Skip empty lines and lines that contain only whitespace.
#    Strip whitespace from each field.
#
# 2. aggregate_by_name(data: list[tuple]) -> dict[str, list[tuple]]
#    Groups the parsed data by sensor name.
#    Returns a dict mapping sensor_name -> list of (value, unit) tuples.
#    Sensors appear in the dict in the order they first appear in the data.
#
# 3. stats_for(sensor_name: str, aggregate: dict[str, list[tuple]]) -> dict | None
#    Returns a dict with keys "mean", "min", "max", "count" for the
#    given sensor, or None if the sensor does not exist in the aggregate.
#    - "mean" is the arithmetic mean of all values (float)
#    - "min" is the minimum value (float)
#    - "max" is the maximum value (float)
#    - "count" is the number of readings (int)
#    Build these by looping through the list — do not use sum(), min(), max(),
#    or len() on the values. You may use len() on the overall list.
#
#
# Example sensor log (sensor_log.txt):
#   temp 21.5 C
#   dist 0.4 m
#   temp 22.0 C
#   dist 0.3 m
#   pressure 1013.25 hPa
#   temp 21.8 C
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 011_aggregate_sensors.py
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

import os

# Create a test log file
test_log = "011_test_log.txt"
with open(test_log, "w") as f:
    f.write("temp 21.5 C\n")
    f.write("dist 0.4 m\n")
    f.write("temp 22.0 C\n")
    f.write("dist 0.3 m\n")
    f.write("\n")  # test that empty lines are skipped
    f.write("   \n")  # test that whitespace-only lines are skipped
    f.write("pressure 1013.25 hPa\n")
    f.write("temp 21.8 C\n")

data = parse_sensor_log(test_log)
assert len(data) == 5, f"Expected 5 rows, got {len(data)}"
assert data[0] == ("temp", 21.5, "C")
assert data[1] == ("dist", 0.4, "m")
assert data[2] == ("temp", 22.0, "C")
assert data[3] == ("pressure", 1013.25, "hPa")
assert data[4] == ("temp", 21.8, "C")

agg = aggregate_by_name(data)
assert set(agg.keys()) == {"temp", "dist", "pressure"}
assert len(agg["temp"]) == 3
assert len(agg["dist"]) == 2
assert len(agg["pressure"]) == 1

stats = stats_for("temp", agg)
assert stats["count"] == 3
assert stats["mean"] == 21.766666666666666  # (21.5 + 22.0 + 21.8) / 3
assert stats["min"] == 21.5
assert stats["max"] == 22.0

assert stats_for("pressure", agg)["mean"] == 1013.25
assert stats_for("pressure", agg)["count"] == 1

assert stats_for("lidar", agg) is None

# Edge: single reading
single_agg = aggregate_by_name([("x", 42.0, "unit")])
single_stats = stats_for("x", single_agg)
assert single_stats["count"] == 1
assert single_stats["mean"] == 42.0
assert single_stats["min"] == 42.0
assert single_stats["max"] == 42.0

# Clean up
os.remove(test_log)

print("ok")
