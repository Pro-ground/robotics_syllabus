# Problem 23 — one node publishes a scan, another publishes a command
#
# One node publishes a fake laser scan. Another reads it and publishes a
# velocity command. Drive the stop distance from a parameter.
#
# Use the Bus from 021 (copied below). Run both sides with ordinary
# function calls. There is no launch file and no colcon workspace.
#
# What you will need
#
# Packages: none.
#
# Ideas to have in place before you start:
# - A scan message here is {"range": number, "stamp": number}.
# - A command message is {"v": number, "w": number}.
# - If the latest range is less than or equal to stop_distance, publish
#   zeros. Otherwise publish a small forward speed.
# - If no scan has arrived yet, publish zeros.
#
# Tools to look up if you do not know them yet:
# - the Bus methods from 021
# - None for "no scan yet"
#
# Snippets
#
#   if latest is None:
#       return {"v": 0.0, "w": 0.0}
#   if latest["range"] <= stop_distance:
#       return {"v": 0.0, "w": 0.0}
#   return {"v": 0.2, "w": 0.0}
#
# ----- Given (do not edit) -----

class Bus:
    def __init__(self):
        self._subs = {}

    def subscribe(self, topic, callback):
        if topic not in self._subs:
            self._subs[topic] = []
        self._subs[topic].append(callback)

    def publish(self, topic, message):
        for callback in self._subs.get(topic, []):
            callback(message)


# ----- EXERCISE -----
#
# 1. make_scan(range_m, stamp)
#    Return {"range": range_m, "stamp": stamp}.
#    Your answer:

def make_scan(range_m, stamp):
    pass


# 2. command_from_scan(scan, stop_distance, forward_speed)
#    scan is a dict or None.
#    Return {"v": 0.0, "w": 0.0} if scan is None or scan["range"] is
#    less than or equal to stop_distance.
#    Otherwise return {"v": forward_speed, "w": 0.0}.
#    Do not change scan.
#    Your answer:

def command_from_scan(scan, stop_distance, forward_speed):
    pass


# 3. run_stack(ranges, stop_distance, forward_speed)
#    ranges is a list of range readings in order.
#    For each range, publish a scan on "scan" with stamp equal to the
#    index (0, 1, 2, ...), then publish the command from the latest scan
#    on "cmd".
#    Return the list of command dicts that were published, in order.
#    Your answer:

def run_stack(ranges, stop_distance, forward_speed):
    pass


# ----- ASSERTION ------

assert make_scan(0.8, 3) == {"range": 0.8, "stamp": 3}

assert command_from_scan(None, 0.4, 0.2) == {"v": 0.0, "w": 0.0}
assert command_from_scan({"range": 0.3, "stamp": 0}, 0.4, 0.2) == {"v": 0.0, "w": 0.0}
assert command_from_scan({"range": 0.4, "stamp": 0}, 0.4, 0.2) == {"v": 0.0, "w": 0.0}
scan = {"range": 0.8, "stamp": 1}
assert command_from_scan(scan, 0.4, 0.2) == {"v": 0.2, "w": 0.0}
assert scan["range"] == 0.8

cmds = run_stack([0.8, 0.3, 1.0], 0.4, 0.2)
assert cmds == [
    {"v": 0.2, "w": 0.0},
    {"v": 0.0, "w": 0.0},
    {"v": 0.2, "w": 0.0},
]
assert run_stack([], 0.4, 0.2) == []

print("ok")
