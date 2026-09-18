# Problem 7 — retries and error handling
# Write a single file, e.g. 007_error_handling.py. No external packages, only the stdlib.
#
# What you will need
#
# Packages: json and time from the standard library. No extra installs.
#
# Ideas to have in place before you start:
# - An exception is an error object Python raises when something fails.
#   You handle it with try / except so the program can choose what to do.
# - A custom exception is a class you define so callers can catch your
#   errors by name.
# - Retry means try again after a short wait. Sleep is that wait. Do not
#   retry a file that exists but contains broken JSON; that will not heal.
#
# Tools to look up if you do not know them yet:
# - try / except
# - raise, and defining a class that inherits from Exception
# - json.load or json.loads
# - time.sleep
# - open and FileNotFoundError (from 006)
# - a for or while loop to attempt several times (from 003)
# - checking that required keys are present in a dict (the in operator)
#
# You do not need: NumPy, environment variables, or extra packages. The
# old title mentioned environment variables; this file does not use them.
#
# 1. read_sensor_with_retry(filename: str, retries: int = 3) -> dict | None
#    Attempts to read a JSON sensor file, handling potential errors gracefully.
#    - The file contains JSON with keys "sensor", "value", and "unit".
#    - If the file exists and is valid JSON, return the parsed dictionary.
#    - If the file does not exist, wait 0.1 seconds and retry.
#    - If the JSON is malformed, log a message and return None immediately (do not retry).
#    - After retries is exhausted, return None.
#    - Return the data dict on success.
#    - Each retry attempt should pause 0.1 seconds using time.sleep(0.1).
#
# 2. read_sensor_safe(filename: str) -> dict
#    Reads a JSON sensor file. On failure, raises a custom exception.
#    - Define a custom exception class called SensorFileError.
#    - If the file does not exist, raise SensorFileError with message
#      "File not found: {filename}".
#    - If the file contains invalid JSON, raise SensorFileError with message
#      "Invalid JSON in {filename}".
#    - If the JSON is missing the required keys ("sensor", "value", "unit"),
#      raise SensorFileError with message
#      "Missing required keys in {filename}".
#    - Return the parsed dictionary on success.
#
#
# Example JSON content (sensor_reading.json):
#   {
#     "sensor": "temp",
#     "value": 21.5,
#     "unit": "C"
#   }
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 007_error_handling.py
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
import json
import time

# --- Helper: write a test JSON file ---
def _write_test_json(path, content):
    with open(path, "w") as f:
        json.dump(content, f)

test_good = "007_test_good.json"
test_bad_json = "007_test_bad.json"
test_missing_keys = "007_test_missing.json"
test_nonexistent = "007_test_gone.json"

good_data = {"sensor": "temp", "value": 21.5, "unit": "C"}
_write_test_json(test_good, good_data)

with open(test_bad_json, "w") as f:
    f.write("{ invalid json }")

_write_test_json(test_missing_keys, {"sensor": "temp", "value": 21.5})

# --- Test read_sensor_safe ---
result = read_sensor_safe(test_good)
assert result == good_data

try:
    read_sensor_safe(test_nonexistent)
    assert False, "Should have raised SensorFileError"
except SensorFileError as e:
    assert f"File not found: {test_nonexistent}" in str(e)

try:
    read_sensor_safe(test_bad_json)
    assert False, "Should have raised SensorFileError"
except SensorFileError as e:
    assert f"Invalid JSON in {test_bad_json}" in str(e)

try:
    read_sensor_safe(test_missing_keys)
    assert False, "Should have raised SensorFileError"
except SensorFileError as e:
    assert "Missing required keys" in str(e)

# --- Test read_sensor_with_retry ---
# Nonexistent file — should retry and eventually return None
result = read_sensor_with_retry(test_nonexistent, retries=3)
assert result is None

# Good file — should succeed immediately
result = read_sensor_with_retry(test_good, retries=3)
assert result == good_data

# Bad JSON — should return None immediately (no retry for parse errors)
result = read_sensor_with_retry(test_bad_json, retries=3)
assert result is None

# Clean up test files
for path in [test_good, test_bad_json, test_missing_keys, test_nonexistent]:
    if os.path.exists(path):
        os.remove(path)

print("ok")
