# Problem 23 — one node publishes a scan, another publishes a command
#
# This file is the worked answer for 023_two_node_stack.py. Try that file first.

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


def make_scan(range_m, stamp):
    return {"range": range_m, "stamp": stamp}


def command_from_scan(scan, stop_distance, forward_speed):
    if scan is None or scan["range"] <= stop_distance:
        return {"v": 0.0, "w": 0.0}
    return {"v": forward_speed, "w": 0.0}


def run_stack(ranges, stop_distance, forward_speed):
    bus = Bus()
    latest = {"scan": None}
    cmds = []

    def on_scan(message):
        latest["scan"] = dict(message)

    def on_cmd(message):
        cmds.append(dict(message))

    bus.subscribe("scan", on_scan)
    bus.subscribe("cmd", on_cmd)
    for i in range(len(ranges)):
        bus.publish("scan", make_scan(ranges[i], i))
        bus.publish("cmd", command_from_scan(latest["scan"], stop_distance, forward_speed))
    return cmds


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
