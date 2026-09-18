# Problem 11 — reading CSV and writing JSON
#
# This file is the worked answer for 011_file_io_json.py. Try that file first.

import json

# ----- EXERCISE -----

def read_sensor_csv(filename):
    rows = []
    header = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = []
            for part in line.split(","):
                parts.append(part.strip())
            if header is None:
                header = parts
                continue
            row = {}
            for i in range(len(header)):
                row[header[i]] = parts[i]
            rows.append(row)
    return rows


def filter_by_sensor(data, sensor_name):
    found = []
    for row in data:
        if row["sensor"] == sensor_name:
            found.append(row)
    return found


def write_sensor_json(data, filename):
    text = json.dumps(data, indent=2)
    with open(filename, "w") as f:
        f.write(text)
        f.write("\n")


# ----- ASSERTION ------

import os

test_csv = "011_test_sensor_data.csv"
with open(test_csv, "w") as f:
    f.write("sensor,value,unit\n")
    f.write("temp,21.5,C\n")
    f.write("dist,0.4,m\n")
    f.write("temp,22.0,C\n")
    f.write("pressure,1013.25,hPa\n")
    f.write("\n")

data = read_sensor_csv(test_csv)
assert len(data) == 4, f"Expected 4 rows, got {len(data)}"
assert data[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
assert data[1] == {"sensor": "dist", "value": "0.4", "unit": "m"}
assert data[2] == {"sensor": "temp", "value": "22.0", "unit": "C"}
assert data[3] == {"sensor": "pressure", "value": "1013.25", "unit": "hPa"}

temps = filter_by_sensor(data, "temp")
assert len(temps) == 2
assert temps[0]["value"] == "21.5"
assert temps[1]["value"] == "22.0"

no_match = filter_by_sensor(data, "lidar")
assert no_match == []
assert data[0]["sensor"] == "temp"

json_file = "011_test_output.json"
write_sensor_json(temps, json_file)

with open(json_file, "r") as f:
    content = f.read()

result = json.loads(content)
assert isinstance(result, list)
assert len(result) == 2
assert result[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
assert result[1] == {"sensor": "temp", "value": "22.0", "unit": "C"}
assert content.endswith("\n")

try:
    read_sensor_csv("does_not_exist.csv")
    assert False, "Should have raised FileNotFoundError"
except FileNotFoundError:
    pass

os.remove(test_csv)
os.remove(json_file)

print("ok")
