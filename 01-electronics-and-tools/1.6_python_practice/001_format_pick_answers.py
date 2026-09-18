# Problem 1 — format a reading and pick values
#
# This file is the worked answer for 001_format_pick.py. Try that file first.

# ----- EXERCISE -----

def format_reading(name, value, unit):
    return f"{name}: {value} {unit}"


def values_for(rows, name):
    found = []
    for row in rows:
        if row[0] == name:
            found.append(row[1])
    return found


# ----- ASSERTION ------

assert format_reading("temp", 21.5, "C") == "temp: 21.5 C"
assert format_reading("dist", 0.4, "m") == "dist: 0.4 m"
assert format_reading("battery", 12, "V") == "battery: 12 V"

rows = [["temp", 21.5], ["dist", 0.4], ["temp", 22.0]]
assert values_for(rows, "temp") == [21.5, 22.0]
assert values_for(rows, "dist") == [0.4]
assert values_for(rows, "pressure") == []
assert rows == [["temp", 21.5], ["dist", 0.4], ["temp", 22.0]]

print("ok")
