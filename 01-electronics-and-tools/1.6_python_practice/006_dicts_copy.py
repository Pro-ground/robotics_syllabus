# Problem 6 — named fields and a copy you made on purpose
#
# A dictionary maps a name to a value. Robot parameters, JSON rows, and
# message-like records all look like this: {"name": "temp", "value": 21.5}.
# A list is still the right shape for a sequence: a scan, a list of
# waypoints, a short history of samples.
#
# Two names can point at the same object. If a callback later changes
# that object, every name sees the change. If a callback must keep its
# own copy, make that copy on purpose.
#
# What you will need
#
# Packages: none. Use only what Python gives you with no install.
#
# Ideas to have in place before you start:
# - row["sensor"] reads the value stored under the name "sensor".
# - row["sensor"] = "temp" writes that name.
# - dict(row) or row.copy() makes a new dictionary with the same keys.
#   The new dictionary is not the same object as row.
# - list(scan) makes a new list with the same items. Changing the new
#   list does not change scan.
# - is tells you whether two names point at the same object. == tells
#   you whether their contents match.
#
# Tools to look up if you do not know them yet:
# - dict, list, .copy()
# - the is operator
#
# You do not need: classes, files, or NumPy.
#
# Snippets
#
#   record = {"name": "temp", "value": 21.5, "unit": "C"}
#   other = record
#   other["value"] = 0
#   # record["value"] is also 0: both names are the same object
#
#   kept = dict(record)
#   kept["value"] = 99
#   # record["value"] is unchanged
#
#   scan = [0.4, 0.5, 0.6]
#   snapshot = list(scan)
#   snapshot[0] = 99
#   # scan[0] is still 0.4
#
# ----- EXERCISE -----
#
# 1. reading_record(name, value, unit)
#    Return a new dictionary with exactly these keys: "name", "value",
#    "unit". Store the three arguments under those keys.
#
#    Examples
#    reading_record("temp", 21.5, "C")
#      ->  {"name": "temp", "value": 21.5, "unit": "C"}
#    Your answer:

def reading_record(name, value, unit):
    pass


# 2. copy_reading(record)
#    record is a dictionary.
#    Return a new dictionary with the same keys and values.
#    Changing the returned dictionary must not change record.
#    Do not return record itself.
#    Your answer:

def copy_reading(record):
    pass


# 3. snapshot_scan(scan)
#    scan is a list of numbers (one range reading per angle).
#    Return a new list with the same items in the same order.
#    Changing the returned list must not change scan.
#    Your answer:

def snapshot_scan(scan):
    pass


# 4. remember_without_alias(history, record)
#    history is a list of dictionaries. record is one dictionary.
#    Return a new list that is the old items plus a copy of record.
#    Do not change history. Do not store record itself; store a copy so
#    a later write to record cannot change what you remembered.
#    Your answer:

def remember_without_alias(history, record):
    pass


# ----- ASSERTION ------

r = reading_record("temp", 21.5, "C")
assert r == {"name": "temp", "value": 21.5, "unit": "C"}
r["value"] = 0
assert reading_record("temp", 21.5, "C")["value"] == 21.5

original = {"name": "dist", "value": 0.4, "unit": "m"}
copied = copy_reading(original)
assert copied == original
assert copied is not original
copied["value"] = 9
assert original["value"] == 0.4

scan = [0.4, 0.5, 0.6]
shot = snapshot_scan(scan)
assert shot == [0.4, 0.5, 0.6]
assert shot is not scan
shot[0] = 99
assert scan == [0.4, 0.5, 0.6]

history = [{"name": "temp", "value": 21.5}]
record = {"name": "temp", "value": 22.0}
out = remember_without_alias(history, record)
assert history == [{"name": "temp", "value": 21.5}]
assert len(out) == 2
assert out[1] == {"name": "temp", "value": 22.0}
assert out[1] is not record
record["value"] = 0
assert out[1]["value"] == 22.0
assert out is not history

print("ok")
