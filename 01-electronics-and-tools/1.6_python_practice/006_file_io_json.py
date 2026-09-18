# Problem 6 — reading CSV and writing JSON
#
# Function 1 is the
# first time you open a file. Function 2 is the same walk as 001 and 003; <- why? It shouldn't be the same as 1. 
# it does not open a file. Function 3 has one new built in: json.dumps.
#
# Do not use the csv module. Do not use csv.DictReader. Those names look
# relevant and they will send you down a different path than this spec.
#
# What you will need
#
# Packages: json for function 3 only (import json). Function 1 and 2 use
# only open, strip, split, and a for loop.
#
# Ideas to have in place before you start:
# - A CSV file is plain text: the first line names the columns, later lines
#   are rows, fields separated by commas.
# - A dictionary maps a name to a value. After you read a row, row["sensor"]
#   is the sensor name as a string.
# - JSON is a text format for lists and dictionaries. It looks like this: 

# <- Insert .json here.


# - open(filename) raises FileNotFoundError if the path does not exist.
#   Do not catch that error in this file.
#
# Look up only if you do not know them yet:
# - Function 1: with open(filename) as f, then for line in f
# - Function 3: json.dumps(data, indent=2), then f.write(...)
# Function 2 needs no lookup. Use values_for from 001 as the model. <-
#
# You do not need: the csv module, NumPy, classes, or pandas.
#
# 1. read_sensor_csv(filename)
#    Open the file and turn it into a list of dictionaries.
#    Do these steps in this order:
#      - with open(filename) as f
#      - For each line in the file:
#          strip the line
#          if the line is now empty, skip it
#          split the line on commas, then strip each piece
#          the first non-empty line is the header (column names); store it
#          each later line is a row: make a dict that maps header[i] to
#          piece[i], keep every value as a string, append the dict
#    Return the list of row dicts.
#    If the file does not exist, let FileNotFoundError through.
#
# 2. filter_by_sensor(data, sensor_name)
#    data is already a list of dictionaries, like the return value of
#    function 1. Do not open a file. Do not import csv.
#    Make a new empty list. For each row in data, if row["sensor"] equals
#    sensor_name, append that row. Return the new list. Do not change data.
#    This is values_for from 001, with dicts instead of [name, number].
#
# 3. write_sensor_json(data, filename)
#    data is a list of dictionaries. Turn it into JSON text and write it.
#    Do these steps in this order:
#      - import json (once, at the top of your code)
#      - text = json.dumps(data, indent=2)
#      - with open(filename, "w") as f: write text, then write a newline
#    Return None.
#
#
# Example CSV content (sensor_data.csv):
#   sensor,value,unit
#   temp,21.5,C
#   dist,0.4,m
#   temp,22.0,C
#   pressure,1013.25,hPa
#
# read_sensor_csv(...)[0]
#   ->  {"sensor": "temp", "value": "21.5", "unit": "C"}
#
# filter_by_sensor(that_list, "temp")  ->  the two temp rows, in order
# filter_by_sensor(that_list, "lidar") ->  []
#

# ----- EXERCISE -----

# 1. read_sensor_csv(filename)
#    Open the file and turn it into a list of dictionaries.
#    Do these steps in this order:
#      - with open(filename) as f
#      - For each line in the file:
#          strip the line
#          if the line is now empty, skip it
#          split the line on commas, then strip each piece
#          the first non-empty line is the header (column names); store it
#          each later line is a row: make a dict that maps header[i] to
#          piece[i], keep every value as a string, append the dict
#    Return the list of row dicts.
#    If the file does not exist, let FileNotFoundError through.

def read_sensor_csv(filename: str) -> list[dict]:
    rows = []
    with open(filename) as f:
        header = None # <- check whether this is explained anywhere. If not, it should be.
        for line in f:
            line = line.strip()
            if line == "":
                continue # <- check if this was taught. Student unlikely to remember this if working on syllabus a few hours a day.
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
    return rows #<- this exercise comprises complex looping operations and this is quite complex for a first task in this module. It should be changed

# 2. filter_by_sensor(data, sensor_name)
#    data is a list of dicts. Do not open a file. Do not use csv.
#    Walk data. If row["sensor"] equals sensor_name, append that row
#    to a new list. Return the new list. Same idea as values_for in 001.

def filter_by_sensor(data, sensor_name):
    output = []
    for row in data:
        if row["sensor"] == sensor_name:
            output.append(row)
    return output

# 3. write_sensor_json(data, filename)
#    data is a list of dictionaries. Turn it into JSON text and write it.
#    Do these steps in this order:
#      - import json
#      - text = json.dumps(data, indent=2)
#      - with open(filename, "w") as f: write text, then write a newline
#    Return None.

import json
def write_sensor_json(data, filename):
    text = json.dumps(data, indent=2)
    with open(filename, "w") as file:
        for line in file:
            print("unedited file: ", line)
        #file.write({"key":"value"})

# ----- ASSERTION ------

import os
import json

# Create a temporary CSV for the tests below
test_csv = "006_test_sensor_data.csv"
with open(test_csv, "w") as f:
    f.write("sensor,value,unit\n")
    f.write("temp,21.5,C\n")
    f.write("dist,0.4,m\n")
    f.write("temp,22.0,C\n")
    f.write("pressure,1013.25,hPa\n")
    f.write("\n")  # test that empty lines are skipped

data = read_sensor_csv(test_csv)
assert len(data) == 4, f"Expected 4 rows, got {len(data)}"
assert data[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
assert data[1] == {"sensor": "dist", "value": "0.4", "unit": "m"}
assert data[2] == {"sensor": "temp", "value": "22.0", "unit": "C"}
assert data[3] == {"sensor": "pressure", "value": "1013.25", "unit": "hPa"}

# Filter
temps = filter_by_sensor(data, "temp")
assert len(temps) == 2
assert temps[0]["value"] == "21.5"
assert temps[1]["value"] == "22.0"

no_match = filter_by_sensor(data, "lidar")
assert no_match == []

# Write and re-read JSON
json_file = "006_test_output.json"
write_sensor_json(temps, json_file)

with open(json_file, "r") as f:
    content = f.read()

result = json.loads(content)
assert isinstance(result, list)
assert len(result) == 2
assert result[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
assert result[1] == {"sensor": "temp", "value": "22.0", "unit": "C"}

# Check trailing newline
assert content.endswith("\n")

FileNotFoundError
try:
    read_sensor_csv("does_not_exist.csv")
    assert False, "Should have raised FileNotFoundError"
except FileNotFoundError:
    pass

# Clean up test files
os.remove(test_csv)
# os.remove(json_file)

print("ok")
