# Problem 1 — format a reading and pick values
#
# What you will need
#
# Packages: none. Use only what Python gives you with no install.
#
# Ideas to have in place before you start:
# - A function is a named piece of code you can call with inputs. It can send
#   a result back with return.
# - A list is an ordered collection. The first item is at position 0, the
#   second at position 1.
# - You compare two values with ==.
#
# Tools to look up if you do not know them yet:
# - An f-string (a string that starts with f) or the format method, for
#   putting values into text
# - list.append(), you build a new list one item at a time
# - A for loop, which enables you to loop through a list item by item (taught in 003; either
#   style is accepted here)
#
# Examples
# format_reading("temp", 21.5, "C")  ->  "temp: 21.5 C"
# format_reading("dist", 0.4, "m")   ->  "dist: 0.4 m"
# format_reading("battery", 12, "V") ->  "battery: 12 V"

# values_for(
#     [["temp", 21.5], ["dist", 0.4], ["temp", 22.0]],
#     "temp",
# )  ->  [21.5, 22.0]

# values_for(..., "pressure")  ->  []

# ----- EXERCISE -----

# 1. format_reading(name, value, unit)
# Return one string in this exact shape (name, colon, space, value, space, unit):
#   temp: 21.5 C
# value may be an int or a float. Use it as-is; do not force extra zeros.

def format_reading(name, value, unit):
    return f"{name}: {value} {unit}"

# 2. values_for(rows, name)
# rows is a list of two-item lists: [sensor_name, number].
# Return a new list of the numbers whose sensor name equals name, in the same order they appear.
# Do not change rows.

def values_for(rows, name):
    return [row[1] for row in rows if row[0] == name]


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
