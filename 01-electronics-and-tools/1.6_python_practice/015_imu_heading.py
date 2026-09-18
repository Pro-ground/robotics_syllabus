# Problem 15 — estimate heading from a fake motion-sensor log
# Write a single file, e.g. 015_imu_heading.py. Requires NumPy.
#
# This file is a short project, not a new topic. Its purpose is to consolidate 
# the learning from all the previous modules. A microcontroller prints one motion-sensor line at a time. Your laptop turns that stream into a
# heading estimate, a forward direction, and a JSON file (a text format
# for lists and dictionaries).
#
# An IMU (inertial measurement unit) here means two sensors on the same
# board: a gyroscope (angular speed, in degrees per second) and an
# accelerometer used as a rough angle in degrees. You already blended
# those two in 014. You already skipped bad lines in 011. File 012 reads
# space-separated logs like the ones here.
#
# Run this in the virtual environment from 010, with NumPy installed.
# Do not import from the earlier files. You may write small helper
# functions. You may use a class; the asserts only check the functions
# below.
#
# What you will need
#
# Packages: json from the standard library, and NumPy (import numpy as np).
#
# Ideas to have in place before you start:
# - Each line is one sample: time t in seconds, gyro_dps, accel_deg,
#   separated by spaces.
# - Bad or empty lines should not crash the parser; skip them.
# - dt (delta time: the change in time) is this sample's t minus the
#   previous sample's t. The heading step is gyro_dps times dt (from 004).
# - Wrap the heading into (-180, 180] the same way as 005.
# - Blend with alpha the same way as 014: trust the gyro side by alpha,
#   and the accelerometer by (1 - alpha).
# - A 2D rotation matrix turns the point [1.0, 0.0] into the robot's
#   forward direction. NumPy's cos and sin use radians.
#
# Tools to look up if you do not know them yet:
# - str.split and float(...) with try / except (from 007 and 011)
# - np.mean, np.radians, np.cos, np.sin, np.array (from 013 and 014)
# - json.dumps with indent=2 (from 006)
#
# You do not need: a real IMU, pyserial, or pandas.
#
# 1. parse_imu_log(filename)
#    Read a text file, one sample per line, fields separated by spaces:
#      t gyro_dps accel_deg
#    Strip whitespace. Skip a line if it is empty, does not have exactly
#    three fields, or any field cannot be turned into a float.
#    If the file does not exist, raise FileNotFoundError (do not catch it).
#    Return a list of dictionaries in file order, each with keys
#    "t", "gyro_dps", and "accel_deg" as floats.
#    An empty file, or a file with no good lines, returns an empty list.
#
# 2. estimate_headings(samples, alpha)
#    samples is the list from parse_imu_log. alpha is a blend weight
#    between 0 and 1.
#    If samples is empty, return an empty list.
#    Start heading at the first sample's accel_deg, wrapped into
#    (-180, 180]. That is the first value in the list you return.
#    For each later sample, in order:
#      dt is this sample's t minus the previous sample's t
#      gyro_guess is heading + (this sample's gyro_dps times dt)
#      heading is wrap(alpha * gyro_guess + (1 - alpha) * this sample's
#      accel_deg)
#      append that heading
#    Return the list of headings, one per sample, as plain Python floats.
#
# 3. run_imu_log(filename, json_filename, alpha)
#    Parse the file. Estimate headings with the given alpha.
#    Build a report dictionary with these keys, in this order:
#      - mean_deg: the mean of the headings as a Python float. Use NumPy.
#        If there are no headings, use 0.0
#      - last_deg: the last heading, or 0.0 if there are none
#      - forward: the point [1.0, 0.0] rotated counter-clockwise by
#        last_deg, as a plain Python list of two floats. Use the same
#        2-by-2 rotation matrix as 014:
#          [cos(θ)  -sin(θ)]
#          [sin(θ)   cos(θ)]
#        Convert last_deg to radians first. If there are no headings,
#        forward is [1.0, 0.0]
#      - label: one string in this exact shape: "heading: <last_deg> deg"
#        Use last_deg as-is; do not force extra zeros.
#    Write the report with json.dumps and indent=2. End the file with a
#    newline.
#    Return the report dictionary.
#
#
# Examples
#
# # File:
# #   0.00 0.0 0.0
# #   0.10 20.0 2.0
# #   bad line
# #   0.20 0.0 2.0
# # With alpha 1.0 the headings are 0.0, then 2.0, then 2.0
# # (first accel is 0; then 0 + 20 * 0.10; then 2 + 0 * 0.10).
# # mean_deg is 4 / 3. last_deg is 2.0. label is "heading: 2.0 deg".
# # forward is the rotation of [1.0, 0.0] by 2 degrees.
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 015_imu_heading.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----
# Write your code below.


# ----- ASSERTION ------
#

import json
import math
import os

import numpy as np

test_log = "015_test_imu.txt"
test_json = "015_test_imu.json"

with open(test_log, "w") as f:
    f.write("0.00 0.0 0.0\n")
    f.write("  0.10  20.0  2.0 \n")
    f.write("\n")
    f.write("bad line\n")
    f.write("0.20 0.0 2.0\n")
    f.write("not,enough\n")

samples = parse_imu_log(test_log)
assert len(samples) == 3
assert abs(samples[0]["t"] - 0.0) < 1e-12
assert abs(samples[0]["gyro_dps"] - 0.0) < 1e-12
assert abs(samples[0]["accel_deg"] - 0.0) < 1e-12
assert abs(samples[1]["t"] - 0.10) < 1e-12
assert abs(samples[1]["gyro_dps"] - 20.0) < 1e-12
assert abs(samples[1]["accel_deg"] - 2.0) < 1e-12
assert abs(samples[2]["t"] - 0.20) < 1e-12

headings = estimate_headings(samples, 1.0)
assert len(headings) == 3
assert abs(headings[0] - 0.0) < 1e-12
assert abs(headings[1] - 2.0) < 1e-12
assert abs(headings[2] - 2.0) < 1e-12

assert estimate_headings([], 0.98) == []

# Wrap: first accel 190 becomes -170. alpha 1.0, gyro 0, heading stays -170.
wrap_samples = [
    {"t": 0.0, "gyro_dps": 0.0, "accel_deg": 190.0},
    {"t": 0.1, "gyro_dps": 0.0, "accel_deg": 190.0},
]
wrapped = estimate_headings(wrap_samples, 1.0)
assert abs(wrapped[0] - (-170)) < 1e-12
assert abs(wrapped[1] - (-170)) < 1e-12

# Blend: first heading 45. One gyro step 10 deg/s for 0.01 s, accel 45,
# alpha 0.98 -> 0.98 * (45 + 0.1) + 0.02 * 45 = 45.098
blend_samples = [
    {"t": 0.0, "gyro_dps": 0.0, "accel_deg": 45.0},
    {"t": 0.01, "gyro_dps": 10.0, "accel_deg": 45.0},
]
blended = estimate_headings(blend_samples, 0.98)
assert abs(blended[0] - 45.0) < 1e-12
assert abs(blended[1] - 45.098) < 1e-6

report = run_imu_log(test_log, test_json, 1.0)
assert abs(report["mean_deg"] - (4.0 / 3.0)) < 1e-12
assert abs(report["last_deg"] - 2.0) < 1e-12
assert report["label"] == "heading: 2.0 deg"
theta = math.radians(2.0)
assert abs(report["forward"][0] - math.cos(theta)) < 1e-9
assert abs(report["forward"][1] - math.sin(theta)) < 1e-9
assert list(report.keys()) == ["mean_deg", "last_deg", "forward", "label"]

with open(test_json) as f:
    content = f.read()
assert content.endswith("\n")
saved = json.loads(content)
assert abs(saved["last_deg"] - 2.0) < 1e-12
assert saved["label"] == "heading: 2.0 deg"

# 90 degrees: forward is [0, 1]
turn_log = "015_test_turn.txt"
with open(turn_log, "w") as f:
    f.write("0.0 0.0 90.0\n")
turn_report = run_imu_log(turn_log, "015_test_turn.json", 1.0)
assert abs(turn_report["last_deg"] - 90.0) < 1e-12
assert abs(turn_report["forward"][0] - 0.0) < 1e-9
assert abs(turn_report["forward"][1] - 1.0) < 1e-9

empty_log = "015_test_empty.txt"
with open(empty_log, "w") as f:
    f.write("\n")
    f.write("nope\n")
empty_report = run_imu_log(empty_log, "015_test_empty.json", 0.98)
assert empty_report["mean_deg"] == 0.0
assert empty_report["last_deg"] == 0.0
assert empty_report["forward"] == [1.0, 0.0]
assert empty_report["label"] == "heading: 0.0 deg"

try:
    parse_imu_log("015_does_not_exist.txt")
    assert False, "Should have raised FileNotFoundError"
except FileNotFoundError:
    pass

os.remove(test_log)
os.remove(test_json)
os.remove(turn_log)
os.remove("015_test_turn.json")
os.remove(empty_log)
os.remove("015_test_empty.json")

print("ok")
