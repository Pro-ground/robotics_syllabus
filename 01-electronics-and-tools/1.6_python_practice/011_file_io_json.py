# Problem 11 — reading CSV and writing JSON
#
# Function 1 is the first time you open a file. Function 2 filters a list
# you already have in memory. Function 3 writes that list out as JSON.
#
# A CSV file is plain text: the first line names the columns, later lines
# are rows, fields separated by commas.
# JSON is a text format for lists and dictionaries. It looks like this:
#
#   [
#     {"sensor": "temp", "value": "21.5", "unit": "C"}
#   ]
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
# - A dictionary maps a name to a value. After you read a row, row["sensor"]
#   is the sensor name as a string.
# - None means "no value yet." Use it for the header until the first
#   non-empty line arrives.
# - continue skips the rest of this pass of a loop and goes to the next
#   item.
# - open(filename) raises FileNotFoundError if the path does not exist.
#   Do not catch that error in this file.
#
# Tools to look up if you do not know them yet:
# - Function 1: with open(filename) as f, then for line in f
# - Function 3: json.dumps(data, indent=2), then f.write(...)
# Function 2 needs no lookup. Use values_for from 001 as the model, with
# dictionaries instead of [name, number].
#
# You do not need: the csv module, NumPy, classes, or pandas.
#
# Snippets
#
#   with open(filename) as f:
#       for line in f:
#           line = line.strip()
#           if line == "":
#               continue
#           parts = line.split(",")
#
#   header = None
#   if header is None:
#       header = parts
#       continue
#
#   row = {}
#   row[header[0]] = parts[0]
#
#   import json
#   text = json.dumps(data, indent=2)
#   with open(filename, "w") as f:
#       f.write(text)
#       f.write("\n")
#
# ----- EXERCISE -----
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
#    Your answer:

def read_sensor_csv(filename):
    pass


# 2. filter_by_sensor(data, sensor_name)
#    data is already a list of dictionaries, like the return value of
#    function 1. Do not open a file. Do not import csv.
#    Make a new empty list. For each row in data, if row["sensor"] equals
#    sensor_name, append that row. Return the new list. Do not change data.
#    Your answer:

def filter_by_sensor(data, sensor_name):
    pass


# 3. write_sensor_json(data, filename)
#    data is a list of dictionaries. Turn it into JSON text and write it.
#    Do these steps in this order:
#      - import json (once, at the top of your code)
#      - text = json.dumps(data, indent=2)
#      - with open(filename, "w") as f: write text, then write a newline
#    Return None.
#    Your answer:

def write_sensor_json(data, filename):
    pass


# ----- ASSERTION ------

import os
import json

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
