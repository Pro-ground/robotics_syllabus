# Problem 6 — reading CSV and writing JSON
# Write a single file, e.g. 006_file_io_json.py. No external packages, only the stdlib.
#
# Do the files in this folder in numbered order. This is 006 of 013.
#
# What you will need
#
# Packages: the csv and json modules from the standard library are enough.
# You may also split lines yourself with str.split. Do not install extra
# packages.
#
# Ideas to have in place before you start:
# - A CSV file is plain text: the first line names the columns, later lines
#   are rows, fields separated by commas.
# - JSON is a text format for nested lists and dictionaries. A JSON array
#   is a list; a JSON object is a dict.
# - open(filename) raises FileNotFoundError if the path does not exist.
#   You do not have to catch that error in read_sensor_csv; letting it
#   through is the required behaviour.
#
# Tools to look up if you do not know them yet:
# - open and a with block, so the file is closed afterwards
# - csv.DictReader, or readline / split / strip if you parse by hand
# - json.dumps (the spec asks for indent=2)
# - writing a string with a file object's write method
# - a for loop over rows (from 003) and dict key lookup
#
# You do not need: NumPy, classes, or pandas.
#
# 1. read_sensor_csv(filename: str) -> list[dict]
#    Reads a CSV file and returns a list of dictionaries.
#    - The first line of the file is the header row.
#    - Each subsequent line is a data row with values separated by commas.
#    - Each dictionary maps column headers to string values (keep values as strings).
#    - Strip whitespace from both headers and values.
#    - Skip any completely empty lines.
#    - If the file does not exist, raise FileNotFoundError.
#
# 2. filter_by_sensor(data: list[dict], sensor_name: str) -> list[dict]
#    Filters the data list to include only rows where the "sensor" column
#    exactly matches sensor_name. Returns a new list; does not modify the input.
#
# 3. write_sensor_json(data: list[dict], filename: str) -> None
#    Writes a list of dictionaries to a JSON file.
#    - The JSON output should be a JSON array of objects (one per dict).
#    - Use json.dumps with indent=2 for readable output.
#    - Ensure the file ends with a newline.
#
#
# Example CSV content (sensor_data.csv):
#   sensor,value,unit
#   temp,21.5,C
#   dist,0.4,m
#   temp,22.0,C
#   pressure,1013.25,hPa
#
#
# Expected usage:
#   data = read_sensor_csv("sensor_data.csv")
#   temps = filter_by_sensor(data, "temp")
#   write_sensor_json(temps, "temps.json")
#

# ----- EXERCISE -----
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

# import os
# import json

# # Create a temporary CSV for the tests below
# test_csv = "006_test_sensor_data.csv"
# with open(test_csv, "w") as f:
#     f.write("sensor,value,unit\n")
#     f.write("temp,21.5,C\n")
#     f.write("dist,0.4,m\n")
#     f.write("temp,22.0,C\n")
#     f.write("pressure,1013.25,hPa\n")
#     f.write("\n")  # test that empty lines are skipped

# data = read_sensor_csv(test_csv)
# assert len(data) == 4, f"Expected 4 rows, got {len(data)}"
# assert data[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
# assert data[1] == {"sensor": "dist", "value": "0.4", "unit": "m"}
# assert data[2] == {"sensor": "temp", "value": "22.0", "unit": "C"}
# assert data[3] == {"sensor": "pressure", "value": "1013.25", "unit": "hPa"}

# # Filter
# temps = filter_by_sensor(data, "temp")
# assert len(temps) == 2
# assert temps[0]["value"] == "21.5"
# assert temps[1]["value"] == "22.0"

# no_match = filter_by_sensor(data, "lidar")
# assert no_match == []

# # Write and re-read JSON
# json_file = "006_test_output.json"
# write_sensor_json(temps, json_file)

# with open(json_file, "r") as f:
#     content = f.read()

# result = json.loads(content)
# assert isinstance(result, list)
# assert len(result) == 2
# assert result[0] == {"sensor": "temp", "value": "21.5", "unit": "C"}
# assert result[1] == {"sensor": "temp", "value": "22.0", "unit": "C"}

# # Check trailing newline
# assert content.endswith("\n")

# # FileNotFoundError
# try:
#     read_sensor_csv("does_not_exist.csv")
#     assert False, "Should have raised FileNotFoundError"
# except FileNotFoundError:
#     pass

# # Clean up test files
# os.remove(test_csv)
# os.remove(json_file)

# print("ok")
