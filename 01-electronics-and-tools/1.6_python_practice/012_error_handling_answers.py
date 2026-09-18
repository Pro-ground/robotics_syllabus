# Problem 12 — retries and named errors
#
# This file is the worked answer for 012_error_handling.py. Try that file first.

import json
import time


class SensorFileError(Exception):
    pass


def read_sensor_safe(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        raise SensorFileError("File not found: " + filename)
    except json.JSONDecodeError:
        raise SensorFileError("Invalid JSON in " + filename)
    required = ("sensor", "value", "unit")
    for key in required:
        if key not in data:
            raise SensorFileError("Missing required keys in " + filename)
    return data


def read_sensor_with_retry(filename, retries=3):
    attempts_left = retries
    while attempts_left > 0:
        try:
            with open(filename) as f:
                return json.load(f)
        except FileNotFoundError:
            attempts_left = attempts_left - 1
            if attempts_left > 0:
                time.sleep(0.1)
        except json.JSONDecodeError:
            return None
    return None


# ----- ASSERTION ------

import os


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
