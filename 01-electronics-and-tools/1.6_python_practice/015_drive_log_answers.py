# Problem 15 — clean a drive log and replay it
#
# This file is the worked answer for 015_drive_log.py. Try that file first.

import json
import math


def wrap_degrees(deg):
    wrapped = (deg + 180) % 360 - 180
    if wrapped == -180:
        return 180
    return wrapped


def load_drive_csv(filename):
    rows = []
    with open(filename) as f:
        header_seen = False
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = []
            for part in line.split(","):
                parts.append(part.strip())
            if not header_seen:
                header_seen = True
                continue
            if len(parts) != 4:
                continue
            try:
                x = float(parts[0])
                y = float(parts[1])
                heading_deg = wrap_degrees(float(parts[2]))
                range_m = float(parts[3])
            except ValueError:
                continue
            if range_m < 0.0:
                range_m = 0.0
            if range_m > 10.0:
                range_m = 10.0
            if range_m <= 0.2:
                command = "stop"
            else:
                command = "forward"
            rows.append({
                "x": x,
                "y": y,
                "heading_deg": heading_deg,
                "range_m": range_m,
                "distance_m": math.hypot(x, y),
                "label": f"range: {range_m} m",
                "command": command,
            })
    return rows


def write_drive_json(rows, filename):
    text = json.dumps(rows, indent=2)
    with open(filename, "w") as f:
        f.write(text)
        f.write("\n")


def process_drive_log(csv_filename, json_filename, period, now_fn, sleep_fn):
    rows = load_drive_csv(csv_filename)
    for _row in rows:
        start = now_fn()
        finish = now_fn()
        leftover = period - (finish - start)
        if leftover < 0:
            leftover = 0.0
        sleep_fn(leftover)
    write_drive_json(rows, json_filename)
    return rows


# ----- ASSERTION ------

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
