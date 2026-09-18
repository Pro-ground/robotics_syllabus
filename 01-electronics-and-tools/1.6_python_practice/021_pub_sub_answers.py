# Problem 21 — send and receive on a named stream
#
# This file is the worked answer for 021_pub_sub.py. Try that file first.

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


def make_command(v, w):
    return {"v": v, "w": w}


def store_latest(box, key):
    def callback(message):
        box[key] = dict(message)
    return callback


def publish_on_timer(bus, topic, make_message):
    def tick(*_args):
        bus.publish(topic, make_message())
    return tick


def run_ticks(timer_fn, n):
    for _ in range(n):
        timer_fn()


# ----- ASSERTION ------

bus = Bus()
box = {}
bus.subscribe("scan", store_latest(box, "scan"))
bus.publish("scan", {"range": 0.4})
assert box["scan"] == {"range": 0.4}
bus.publish("scan", {"range": 0.2})
assert box["scan"]["range"] == 0.2
first = box["scan"]
bus.publish("scan", {"range": 1.0})
assert first["range"] == 0.2

cmd = make_command(0.3, -0.1)
assert cmd == {"v": 0.3, "w": -0.1}

sent = []
out_bus = Bus()
out_bus.subscribe("cmd", sent.append)
tick = publish_on_timer(out_bus, "cmd", lambda: make_command(0.5, 0.0))
run_ticks(tick, 3)
assert len(sent) == 3
assert sent[0] == {"v": 0.5, "w": 0.0}

run_ticks(tick, 0)
assert len(sent) == 3

print("ok")
