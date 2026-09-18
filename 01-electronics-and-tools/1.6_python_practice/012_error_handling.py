# Problem 12 — retries and named errors
#
# An exception is an error object Python raises when something fails.
# You handle it with try / except so the program can choose what to do.
# A custom exception is a class you define so callers can catch your
# errors by name. Retry means try again after a short wait.
#
# Do not retry a file that exists but contains broken JSON; that will not
# heal. Sleep is the wait between tries.
#
# What you will need
#
# Packages: json and time from the standard library. No extra installs.
#
# Ideas to have in place before you start:
# - FileNotFoundError means the path does not exist (from 011).
# - json.load reads a file object. json.JSONDecodeError means the text is
#   not valid JSON.
# - "key in dict" is True when that name is present.
# - logging is the usual way to record a problem instead of print. You may
#   use print in this file; the asserts do not check the log text.
#
# Tools to look up if you do not know them yet:
# - try / except
# - raise, and defining a class that inherits from Exception
# - json.load
# - time.sleep
# - a for or while loop to attempt several times (from 003)
#
# You do not need: NumPy, environment variables, or extra packages.
#
# Snippets
#
#   class SensorFileError(Exception):
#       pass
#
#   try:
#       with open(filename) as f:
#           data = json.load(f)
#   except FileNotFoundError:
#       raise SensorFileError("File not found: " + filename)
#   except json.JSONDecodeError:
#       return None
#
#   if "sensor" not in data:
#       raise SensorFileError("Missing required keys in " + filename)
#
#   time.sleep(0.1)
#
# Example JSON content (sensor_reading.json):
#   {
#     "sensor": "temp",
#     "value": 21.5,
#     "unit": "C"
#   }
#
# ----- EXERCISE -----
#
# 1. SensorFileError
#    Define a custom exception class called SensorFileError. It should
#    inherit from Exception. You will raise it from read_sensor_safe.
#    Your answer:

class SensorFileError(Exception):
    pass


# 2. read_sensor_safe(filename)
#    Read a JSON sensor file. On failure, raise SensorFileError.
#    - If the file does not exist, raise SensorFileError with message
#      "File not found: {filename}".
#    - If the file contains invalid JSON, raise SensorFileError with message
#      "Invalid JSON in {filename}".
#    - If the JSON is missing the required keys ("sensor", "value", "unit"),
#      raise SensorFileError with message
#      "Missing required keys in {filename}".
#    - Return the parsed dictionary on success.
#    Your answer:

def read_sensor_safe(filename):
    pass


# 3. read_sensor_with_retry(filename, retries=3)
#    Try to read a JSON sensor file, handling some failures without raising.
#    - The file contains JSON with keys "sensor", "value", and "unit".
#    - If the file exists and is valid JSON, return the parsed dictionary.
#    - If the file does not exist, wait 0.1 seconds and try again.
#    - If the JSON is malformed, return None immediately (do not retry).
#    - After retries is exhausted, return None.
#    - Each retry attempt should pause 0.1 seconds using time.sleep(0.1).
#    retries is how many attempts you get, including the first try.
#    Your answer:

def read_sensor_with_retry(filename, retries=3):
    pass


# ----- ASSERTION ------

import os
import json
import time


def _write_test_json(path, content):
    with open(path, "w") as f:
        json.dump(content, f)


test_good = "012_test_good.json"
test_bad_json = "012_test_bad.json"
test_missing_keys = "012_test_missing.json"
test_nonexistent = "012_test_gone.json"

good_data = {"sensor": "temp", "value": 21.5, "unit": "C"}
_write_test_json(test_good, good_data)

with open(test_bad_json, "w") as f:
    f.write("{ invalid json }")

_write_test_json(test_missing_keys, {"sensor": "temp", "value": 21.5})

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

result = read_sensor_with_retry(test_nonexistent, retries=3)
assert result is None

result = read_sensor_with_retry(test_good, retries=3)
assert result == good_data

result = read_sensor_with_retry(test_bad_json, retries=3)
assert result is None

for path in [test_good, test_bad_json, test_missing_keys, test_nonexistent]:
    if os.path.exists(path):
        os.remove(path)

print("ok")
