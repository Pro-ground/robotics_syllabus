# Problem 27 — one closed loop
#
# This file is the worked answer for 027_closed_loop.py. Try that file first.

import math


def wrap_angle(rad):
    wrapped = (rad + math.pi) % (2 * math.pi) - math.pi
    if wrapped == -math.pi:
        return math.pi
    return wrapped


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def command_to_point(pose, target, v, gain, max_w):
    desired = math.atan2(target["y"] - pose["y"], target["x"] - pose["x"])
    error = wrap_angle(desired - pose["theta"])
    return {"v": v, "w": clamp(gain * error, -max_w, max_w)}


def is_finite_command(cmd):
    return math.isfinite(cmd["v"]) and math.isfinite(cmd["w"])


def apply_watchdog(cmd, now, last_good_time, timeout):
    if not is_finite_command(cmd):
        return {"v": 0.0, "w": 0.0}
    if now - last_good_time > timeout:
        return {"v": 0.0, "w": 0.0}
    return dict(cmd)


def integrate_odom(pose, wheel_v, wheel_w, dt):
    return {
        "x": pose["x"] + wheel_v * math.cos(pose["theta"]) * dt,
        "y": pose["y"] + wheel_v * math.sin(pose["theta"]) * dt,
        "theta": wrap_angle(pose["theta"] + wheel_w * dt),
    }


def step_closed_loop(pose, target, scan, now, last_good_time, params):
    timeout = params["timeout"]
    if scan is None or now - scan["stamp"] > timeout or scan["range"] <= params["stop_distance"]:
        cmd = {"v": 0.0, "w": 0.0}
    else:
        cmd = command_to_point(
            pose, target, params["v"], params["gain"], params["max_w"]
        )
    cmd = apply_watchdog(cmd, now, last_good_time, timeout)
    new_pose = integrate_odom(pose, cmd["v"], cmd["w"], params["dt"])
    return {"pose": new_pose, "cmd": cmd}


# ----- ASSERTION ------

params = {
    "stop_distance": 0.4,
    "v": 0.5,
    "gain": 2.0,
    "max_w": 1.0,
    "timeout": 0.3,
    "dt": 0.1,
}

pose = {"x": 0.0, "y": 0.0, "theta": 0.0}
target = {"x": 2.0, "y": 0.0}

out = step_closed_loop(pose, target, {"range": 1.0, "stamp": 1.0}, 1.05, 1.0, params)
assert abs(out["cmd"]["v"] - 0.5) < 1e-12
assert abs(out["cmd"]["w"] - 0.0) < 1e-12
assert abs(out["pose"]["x"] - 0.05) < 1e-12
assert pose["x"] == 0.0

stopped = step_closed_loop(pose, target, {"range": 0.2, "stamp": 1.0}, 1.05, 1.0, params)
assert stopped["cmd"] == {"v": 0.0, "w": 0.0}
assert abs(stopped["pose"]["x"] - 0.0) < 1e-12

stale = step_closed_loop(pose, target, {"range": 1.0, "stamp": 0.5}, 1.05, 0.5, params)
assert stale["cmd"] == {"v": 0.0, "w": 0.0}

empty = step_closed_loop(pose, target, None, 1.05, 1.0, params)
assert empty["cmd"] == {"v": 0.0, "w": 0.0}

print("ok")
