# Problem 21 — send and receive on a named stream
#
# A node is one running program. A topic is a named stream of messages.
# A publisher sends a message on a topic. A subscription runs a callback
# (a function) when a message arrives. A timer calls a function on a
# fixed period.
#
# This file fakes that graph in ordinary Python so you can run
#   python 021_pub_sub.py
# with no ROS 2 install. The Bus object below is given. You write the
# node functions that use it.
#
# What you will need
#
# Packages: none.
#
# Ideas to have in place before you start:
# - bus.publish(topic, message) delivers message to every callback
#   subscribed to that topic.
# - bus.subscribe(topic, callback) registers callback.
# - A callback should return quickly. Do the work, store what you need,
#   return None.
# - Parameters are named settings, often loaded from a file as in 017.
#
# Tools to look up if you do not know them yet:
# - passing a function as an argument (from 004)
# - dictionaries for messages (from 006)
#
# You do not need: rclpy, colcon, or a workspace.
#
# Snippets
#
#   bus.subscribe("scan", on_scan)
#   bus.publish("cmd", {"v": 0.2, "w": 0.0})
#
#   def on_scan(message):
#       latest["range"] = message["range"]
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
# 1. make_command(v, w)
#    Return a dictionary {"v": v, "w": w}.
#    Your answer:

def make_command(v, w):
    pass


# 2. store_latest(box, key)
#    Return a callback that, when called with a message, writes
#    box[key] = a copy of the message (not the message object itself).
#    Your answer:

def store_latest(box, key):
    pass


# 3. publish_on_timer(bus, topic, make_message)
#    Return a callback that takes no useful payload (the timer will call
#    it with no arguments, or with an ignored tick). When called, it
#    should publish make_message() on topic.
#    Accept either timer() or timer(tick).
#    Your answer:

def publish_on_timer(bus, topic, make_message):
    pass


# 4. run_ticks(timer_fn, n)
#    Call timer_fn n times. n is an integer >= 0. Return None.
#    Your answer:

def run_ticks(timer_fn, n):
    pass


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
