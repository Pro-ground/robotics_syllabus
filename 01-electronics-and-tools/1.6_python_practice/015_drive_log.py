# Problem 15 — clean a drive log and replay it
#
# This file is one short task, not a new topic. It asks you to use
# 001–012 together: format a reading, decide, loop, keep time, wrap an
# angle, read a CSV file, skip bad input, and write JSON.
#
# Do not import from the earlier files. You may write small helper
# functions. Do not call time.sleep; call the sleep_fn you were given.
#
# What you will need
#
# Packages: math and json from the standard library.
#
# Ideas to have in place before you start:
# - A robot log is often a CSV file with some empty or broken lines.
# - Heading is an angle in degrees. Wrap it into the range (-180, 180]
#   the same way as 005: 180 stays 180, and -180 becomes 180.
# - range_m is how far the nearest object is, in metres. Keep it between
#   0.0 and 10.0.
# - A period is how long one replay pass should last, in seconds. The
#   leftover wait is period minus how long this pass already took. If the
#   pass ran long, wait 0.0 seconds.
#
# Tools to look up if you do not know them yet:
# - open and a with block (from 011)
# - try / except around float(...) (from 012)
# - math.hypot for straight-line distance (from 005)
# - now_fn / sleep_fn / leftover wait (from 004)
# - json.dumps with indent=2 (from 011)
#
# You do not need: NumPy, classes, or a real robot.
#
# Snippets
#
#   try:
#       x = float(parts[0])
#   except ValueError:
#       continue
#
#   heading = wrap_degrees(heading)
#   if range_m < 0.0:
#       range_m = 0.0
#   if range_m > 10.0:
#       range_m = 10.0
#
#   leftover = period - elapsed
#   if leftover < 0:
#       leftover = 0.0
#   sleep_fn(leftover)
#
# ----- EXERCISE -----
#
# 1. load_drive_csv(filename)
#    Read a CSV file whose first line is the header:
#      x,y,heading_deg,range_m
#    Each later line is one pose. Strip whitespace from each field.
#    Skip a line if it is empty, or if it does not have four fields, or if
#    any field cannot be turned into a float. Do not raise on a bad line.
#    If the file does not exist, raise FileNotFoundError (do not catch it).
#    For each good row, return a dictionary with these keys:
#      - x, y: the positions as floats
#      - heading_deg: the heading, wrapped into (-180, 180]
#      - range_m: the range, limited to 0.0 if it was below 0.0 and to
#        10.0 if it was above 10.0
#      - distance_m: straight-line distance from (0, 0) to (x, y)
#      - label: one string in this exact shape: "range: <range_m> m"
#        Use the limited range_m. Do not force extra zeros.
#      - command: "stop" if range_m is less than or equal to 0.2,
#        otherwise "forward"
#    Return the list of dictionaries in file order. A file with only a
#    header, or with no good rows, returns an empty list.
#    Your answer:

def load_drive_csv(filename):
    pass


# 2. write_drive_json(rows, filename)
#    Write rows (a list of dictionaries) to a JSON file.
#    Use json.dumps with indent=2. End the file with a newline.
#    Return None.
#    Your answer:

def write_drive_json(rows, filename):
    pass


# 3. process_drive_log(csv_filename, json_filename, period, now_fn, sleep_fn)
#    Load the CSV with load_drive_csv. Then replay each loaded row at a
#    fixed period, the same way as 004:
#      - Record the start time by calling now_fn() with no arguments.
#      - The work for this pass is the row you already loaded. You do not
#        have to compute it again.
#      - Record the time again with now_fn().
#      - elapsed is (time after the row) minus (start time).
#      - Call sleep_fn(leftover), where leftover is period minus elapsed
#        when that is positive, and 0.0 when the pass already ran long.
#    Do not sleep for skipped or missing rows. If the loaded list is
#    empty, do not call now_fn or sleep_fn.
#    After the replay, write the loaded rows with write_drive_json.
#    Return the same list of dictionaries.
#    Your answer:

def process_drive_log(csv_filename, json_filename, period, now_fn, sleep_fn):
    pass


# ----- ASSERTION ------

import json
import os

test_csv = "015_test_drive.csv"
test_json = "015_test_drive.json"

with open(test_csv, "w") as f:
    f.write("x,y,heading_deg,range_m\n")
    f.write("3.0, 4.0, 190, 0.15\n")
    f.write("0.0,0.0,-190,12.0\n")
    f.write("nope,this,is,bad\n")
    f.write("1.0,0.0,360,-1.0\n")
    f.write("\n")
    f.write("0.0,1.0,180,0.2\n")

rows = load_drive_csv(test_csv)
assert len(rows) == 4

assert abs(rows[0]["x"] - 3.0) < 1e-12
assert abs(rows[0]["y"] - 4.0) < 1e-12
assert abs(rows[0]["heading_deg"] - (-170)) < 1e-12
assert abs(rows[0]["range_m"] - 0.15) < 1e-12
assert abs(rows[0]["distance_m"] - 5.0) < 1e-12
assert rows[0]["label"] == "range: 0.15 m"
assert rows[0]["command"] == "stop"

assert abs(rows[1]["heading_deg"] - 170) < 1e-12
assert abs(rows[1]["range_m"] - 10.0) < 1e-12
assert abs(rows[1]["distance_m"] - 0.0) < 1e-12
assert rows[1]["label"] == "range: 10.0 m"
assert rows[1]["command"] == "forward"

assert abs(rows[2]["heading_deg"] - 0) < 1e-12
assert abs(rows[2]["range_m"] - 0.0) < 1e-12
assert abs(rows[2]["distance_m"] - 1.0) < 1e-12
assert rows[2]["label"] == "range: 0.0 m"
assert rows[2]["command"] == "stop"

assert abs(rows[3]["heading_deg"] - 180) < 1e-12
assert abs(rows[3]["range_m"] - 0.2) < 1e-12
assert abs(rows[3]["distance_m"] - 1.0) < 1e-12
assert rows[3]["label"] == "range: 0.2 m"
assert rows[3]["command"] == "stop"

write_drive_json(rows, test_json)
with open(test_json) as f:
    content = f.read()
assert content.endswith("\n")
loaded = json.loads(content)
assert loaded[0]["command"] == "stop"
assert abs(loaded[0]["heading_deg"] - (-170)) < 1e-12

sleeps = []
times = [0.0, 0.005, 1.0, 1.03, 2.0, 2.001, 3.0, 3.0]


def now_fn():
    return times.pop(0)


def sleep_fn(seconds):
    sleeps.append(seconds)


out = process_drive_log(test_csv, test_json, 0.02, now_fn, sleep_fn)
assert len(out) == 4
assert len(sleeps) == 4
assert abs(sleeps[0] - 0.015) < 1e-12
assert sleeps[1] == 0.0
assert abs(sleeps[2] - 0.019) < 1e-12
assert abs(sleeps[3] - 0.02) < 1e-12
assert times == []

try:
    load_drive_csv("015_does_not_exist.csv")
    assert False, "Should have raised FileNotFoundError"
except FileNotFoundError:
    pass

header_only = "015_test_empty.csv"
with open(header_only, "w") as f:
    f.write("x,y,heading_deg,range_m\n")
empty_sleeps = []
empty_rows = process_drive_log(
    header_only,
    "015_test_empty.json",
    0.02,
    lambda: 0.0,
    empty_sleeps.append,
)
assert empty_rows == []
assert empty_sleeps == []

os.remove(test_csv)
os.remove(test_json)
os.remove(header_only)
os.remove("015_test_empty.json")

print("ok")
