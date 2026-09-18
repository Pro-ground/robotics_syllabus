# Problem 6 — named fields and a copy you made on purpose
#
# This file is the worked answer for 006_dicts_copy.py. Try that file first.

def reading_record(name, value, unit):
    return {"name": name, "value": value, "unit": unit}


def copy_reading(record):
    return dict(record)


def snapshot_scan(scan):
    return list(scan)


def remember_without_alias(history, record):
    remembered = list(history)
    remembered.append(dict(record))
    return remembered


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
